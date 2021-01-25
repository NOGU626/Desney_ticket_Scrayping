#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from instagram_private_api import Client, ClientCompatPatch
from PIL import Image
import io
import urllib.request

user_name = 'nogu__1230'
password = 'nogu8940626'
api = Client(user_name, password)

# 画像のURL
# url = "https://www.starbucks.co.jp/cafe/melty_chocolate/images/bg-01.jpg"
url = "https://user-images.githubusercontent.com/5179467/57978324-23e4b000-7a46-11e9-8b04-4d16e97a702c.jpg"
# 画像データを取得する
img_in = urllib.request.urlopen(url).read()
img_bin = io.BytesIO(img_in)
img = Image.open(img_bin)
# 画像を投稿する
api.post_photo_story(img_bin.getvalue(), (100, 100))
# api.post_photo(img_bin.getvalue(), (img.width, img.height),'This is #test')