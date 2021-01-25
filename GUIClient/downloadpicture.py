from selenium import webdriver
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import urllib.request

options = Options()
# ヘッドレスモードを有効にする（次の行をコメントアウトすると画面が表示される）。
options.add_argument('--headless')

driver = webdriver.Chrome(executable_path='/Users/nogu/Desktop/instagram/GUIClient/chromedriver',chrome_options=options)
url = "file:///Users/nogu/Desktop/instagram/GUIClient/index.html"
driver.get(url)
file_url = driver.find_element_by_tag_name("a").get_attribute("href")
urllib.request.urlretrieve(file_url, "/Users/nogu/Desktop/table.png")
