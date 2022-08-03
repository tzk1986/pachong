# -*- coding:utf-8 -*-
"""
@Author:tang
@File:selenium_sample.py
@Time:2022/5/24 14:19
说明：使用selenium抓取页面数据，以避免js错乱反爬机制，直接模拟人操作抓取数据
"""
import time
from selenium import webdriver  # 允许启动浏览器
from selenium.webdriver.common.by import By  # 允许带参数搜索
from selenium.webdriver.support.ui import WebDriverWait  # 允许等待页面加载
from selenium.webdriver.support import expected_conditions as EC  # 判断网页是否加载完毕
from selenium.common.exceptions import TimeoutException  # 处理超时情况
from tqdm import tqdm
import pandas as pd

driver_option = webdriver.ChromeOptions()
driver_option.add_argument(" — incognito")
chromedriver_path = '/usr/local/bin/chromedriver'  # Change this to your own chromedriver path!


def create_webdriver():
    return webdriver.Chrome(executable_path=chromedriver_path, chrome_options=driver_option)


browser = create_webdriver()
browser.get("https://github.com/collections/machine-learning")

# 获取页面中所有project名称
projects = browser.find_elements(by=By.XPATH, value="//h1[@class='h3 lh-condensed']")

# 存放每个project信息
project_list = {}
for proj in tqdm(projects):
    proj_name = proj.text  # Project name
    proj_url = proj.find_elements_by_xpath("a")[0].get_attribute('href')  # Project URL
    project_list[proj_name] = proj_url

# print(project_list)

# 使用字典类型方式传入数据框
project_df = pd.DataFrame.from_dict(project_list, orient='index')
# print(project_df)
# 优化数据展示
project_df['project_name'] = project_df.index
project_df.columns = ['project_url', 'project_name']
project_df = project_df.reset_index(drop=True)
# print(project_df)
# 存入到csv
project_df.to_csv('project_list.csv')

time.sleep(3)
browser.quit()


# 并行执行命令，提高爬虫效率
# from concurrent.futures import ProcessPoolExecutor
# import concurrent.futures
#
#
# def scrape_url(url):
#     new_browser = create_webdriver()
#     new_browser.get(url)
#
#     # Extract required data here
#     # ...
#
#     new_browser.quit()
#
#     return data
#
#
# with ProcessPoolExecutor(max_workers=4) as executor:
#     future_results = {executor.submit(scrape_url, url) for url in urlarray}
#
# results = []
# for future in concurrent.futures.as_completed(future_results):
#     results.append(future.result())
