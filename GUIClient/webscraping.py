#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import datetime
from dateutil.relativedelta import relativedelta

import sys
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup

# チケット処理の繰り返し処理の部分
def ticket_scraping_main():
    num = 0
    dateinfo = ""
    # GUIクライアント様の配列
    return_data = []
    while num < 3:
        info = access_to_site(COUNTER=num,DATETIME = dateinfo)
        return_data.extend(info[0])
        dateinfo = info[1]
        num += 1
    return return_data

# 日本語表記の年月をdatetimeに変換する関数
def hizuke_to_transferdatetime(text):
    date = text.replace("年",",").replace("月","").split(",")
    return datetime.date(int(date[0]),int(date[1]),1)

# 取得したdatetimeを元に日付分加算した結果をreturn
def add_moth_datetime(date,month):
    calc_source = date + relativedelta(months=month)
    return calc_source

# PyInstallerのリソース参照用の関数
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


def access_to_site(URL="https://www.tokyodisneyresort.jp/ticket/sales_status.html",COUNTER = 0,DATETIME = ""):
    # 翌月のカレンダーを表示するための処理
    if(COUNTER != 0 and DATETIME != ""):
        URL = "https://www.tokyodisneyresort.jp/ticket/sales_status/{0}".format(add_moth_datetime(DATETIME,1).strftime("%Y%m"))

    options = Options()
    # ヘッドレスモードを有効にする（次の行をコメントアウトすると画面が表示される）。
    options.add_argument('--headless')
    # ここにUAを書きます。今回はiPhoneでsafari
    options.add_argument('--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36')
    # driver = webdriver.Chrome(executable_path='/Users/nogu/Desktop/instagram/GUIClient/chromedriver')
    driver = webdriver.Chrome(executable_path=resource_path("chromedriver"),chrome_options=options)
    driver.get(URL)
    time.sleep(0.2)

    html = driver.page_source.encode('utf-8')
    time.sleep(0.2)
    driver.close()

    soup = BeautifulSoup(html, 'lxml')

    # データタイム型で当該カレンダーの情報を取得
    date_info = hizuke_to_transferdatetime(soup.find("h2", class_="heading2").text)

    calender = soup.find("table", class_="calendarTableSp ticketStock")
    tbody = calender.find("tbody")
    days = tbody.find_all("tr")
    desny_info = []
    for day in days:
        if day.find("div",class_="day") != None:
            date = str(date_info.year) + "-" +str(date_info.month) + "-" +(day.find("div",class_="day").text)[0:2]
            tdl = day.find("td",class_="tdl").get('class')[1]
            tds = day.find("td",class_="tds").get('class')[1]
            desny_info.append(
                {
                    "date": date.replace("(",""),
                    "TDL": tdl,
                    "TDS": tds
                }
            )
    return desny_info,date_info

# if __name__ == '__main__':
#     reso.main()