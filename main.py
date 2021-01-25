#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from instagram_private_api import Client, ClientCompatPatch

user_name = 'nogu__1230'
password = 'nogu8940626'

api = Client(user_name, password)
results = api.feed_timeline()
print(results)