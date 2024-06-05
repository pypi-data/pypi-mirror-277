# The MIT License (MIT)
#
# Copyright (c) 2024 Scott Lau
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import logging

from sc_utilities import Singleton
from sc_utilities import log_init

log_init()

import pandas as pd
from sc_config import ConfigUtils
from sc_sme_enterprise_search import PROJECT_NAME, __version__
import argparse
import requests
from bs4 import BeautifulSoup
import urllib
import urllib.parse
from sc_utilities import calculate_column_index
from config42 import ConfigManager
import os


def calculate_column_index_from_config(config: ConfigManager, key: str) -> int:
    initial_fund_amount_column_config = config.get(key)
    try:
        return calculate_column_index(initial_fund_amount_column_config)
    except ValueError as e:
        logging.getLogger(__name__).error("configuration {} is invalid".format(key), exc_info=e)
        raise e


class Runner(metaclass=Singleton):

    def __init__(self):
        project_name = PROJECT_NAME
        ConfigUtils.clear(project_name)
        self._config = ConfigUtils.get_config(project_name)
        # 生成的目标Excel文件存放路径
        self._target_directory = self._config.get("output.target_directory")
        # 目标文件名称
        self._target_filename = self._config.get("output.target_filename")
        self._target_sheet_name = self._config.get("output.target_sheet_name")
        self._search_url = self._config.get("env.search_url")
        self._search_param_name = self._config.get("env.search_param_name")
        self._enterprise_url_prefix = self._config.get("env.enterprise_url_prefix")
        self._search_result_element = self._config.get("search.search_result_element")
        self._search_result_id = self._config.get("search.search_result_id")
        self._region_element = self._config.get("search.region_element")
        self._region_keyword = self._config.get("search.region_keyword")

        self._src_filepath = self._config.get("search.source_file_path")
        self._sheet_name = self._config.get("search.sheet_name")
        self._header_row = self._config.get("search.sheet_config.header_row")
        self._name_column = calculate_column_index_from_config(
            self._config, "search.sheet_config.name_column"
        )
        self._name_column_name = None

    def run(self, *, args):
        logging.getLogger(__name__).info("arguments {}".format(args))
        logging.getLogger(__name__).info("program {} version {}".format(PROJECT_NAME, __version__))
        logging.getLogger(__name__).info("configurations {}".format(self._config.as_dict()))

        logging.getLogger(__name__).info("读取源文件：{}".format(self._src_filepath))
        data = pd.read_excel(self._src_filepath, sheet_name=self._sheet_name, header=self._header_row)
        self._name_column_name = data.columns[self._name_column]

        # 初始化 DataFrame
        df = pd.DataFrame(columns=["客户名称", "行政区划代码"])
        index = 0
        for row_i, row in data.iterrows():
            company_name = row[self._name_column_name]
            row = list()
            row.append(company_name)
            region_code = self._find_region_code(company_name=company_name)
            logging.getLogger(__name__).info("公司：[%s] 的行政区划为 [%s] ", company_name, region_code)
            row.append(region_code)
            df.loc[index] = row
            index = index + 1

        target_filename_full_path = os.path.join(self._target_directory, self._target_filename)
        # 如果文件已经存在，则删除
        if os.path.exists(target_filename_full_path):
            logging.getLogger(__name__).info("删除输出文件：%s ", target_filename_full_path)
            try:
                os.remove(target_filename_full_path)
            except Exception as e:
                logging.getLogger(__name__).error("删除输出文件 {} 失败：{} ".format(target_filename_full_path, e))
                return 1

        logging.getLogger(__name__).info("写输出文件：%s ", target_filename_full_path)
        with pd.ExcelWriter(target_filename_full_path) as excel_writer:
            df.to_excel(
                excel_writer=excel_writer,
                index=False,
                sheet_name=self._target_sheet_name,
            )
        return 0

    def _find_region_code(self, company_name):
        headers = {
            "content-type": "text/html; charset=utf-8",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        }
        logging.getLogger(__name__).info("查找公司：{0}".format(company_name))
        response = requests.get(url=self._search_url, headers=headers,
                                params={self._search_param_name: company_name})
        status_code = response.status_code
        if status_code != 200:
            logging.getLogger(__name__).error("请求失败，错误码：{0}".format(status_code))
            return ""
        response_text = response.text
        soup = BeautifulSoup(response_text, 'lxml')
        search_result = soup.find(self._search_result_element, attrs={'id': self._search_result_id})
        if search_result is None:
            logging.getLogger(__name__).error("没有找到对应公司")
            return ""
        links = search_result.find_all('a')
        for link in links:
            if 'href' in link.attrs:
                href_ = link.attrs['href']
                if self._enterprise_url_prefix in href_ and "name" in href_:
                    quoted_url = urllib.parse.quote(href_, safe="/:")
                    response_detail = requests.get(url=quoted_url, headers=headers)
                    status_code2 = response_detail.status_code
                    if status_code2 != 200:
                        logging.getLogger(__name__).error("请求详细信息失败，错误码：{0}".format(status_code2))
                        return ""
                    response_detail_text = response_detail.text
                    soup = BeautifulSoup(response_detail_text, 'lxml')
                    search_region_result = soup.find(self._region_element, text=self._region_keyword)
                    if search_region_result is None:
                        logging.getLogger(__name__).error("没有找到行政区划列表")
                        return ""
                    region_code_list = search_region_result.parent.find_all('span', attrs={'class': 'field-item'})
                    if region_code_list is None:
                        logging.getLogger(__name__).error("没有找到行政区划编码")
                        return ""
                    if len(region_code_list) > 0:
                        return region_code_list[len(region_code_list) - 1].text
        return ""


def main():
    try:
        parser = argparse.ArgumentParser(description='Python project')
        args = parser.parse_args()
        state = Runner().run(args=args)
    except Exception as e:
        logging.getLogger(__name__).exception('An error occurred.', exc_info=e)
        return 1
    else:
        return state
