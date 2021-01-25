#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os

# PyInstallerのリソース参照用の関数
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)

def main():
    print("Hi")

if __name__ == '__main__':
    main()