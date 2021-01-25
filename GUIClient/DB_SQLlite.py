#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3

import sys
import os

class OriginalSQLLite3:
    # コンストラクタ インスタンスを生成したときに一度だけ呼び出されるメソッド
    def __init__(self,dbname):
        self.dbname = dbname
        self.conn = sqlite3.connect(self.dbname)

    def __del__(self):
        # データベースへのコネクションを閉じる。(必須)
        self.conn.close()

    def executeSQL(self, SQL_query):
        # sqliteを操作するカーソルオブジェクトを作成
        self.cur = self.conn.cursor()

        self.cur.execute(SQL_query)
        # データベースへコミット。これで変更が反映される。
        self.conn.commit()
        self.cur.close()

    def fetchallSQL(self,SQL_query):
        self.cur = self.conn.cursor()
        self.cur.execute(SQL_query)
        # 中身を全て取得するfetchall()を使って、printする。
        print(self.cur.fetchall())
        self.cur.close()

# PyInstallerのリソース参照用の関数
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# ディズニー情報を格納するための関数
def desney_data_chiket_Initialize():
    DB = OriginalSQLLite3(dbname=resource_path("DB/SQL.db"))
    DB.executeSQL('DROP TABLE IF EXISTS disneyticket;')
    DB.executeSQL('CREATE TABLE IF NOT EXISTS disneyticket(id INTEGER PRIMARY KEY AUTOINCREMENT,date TEXT,TDL STRING,TDS STRING)')

# ディズニー情報をインサートする関数
def desney_data_chiket_Incert(date,infoTDL,infoTDS):
    DB = OriginalSQLLite3(dbname=resource_path("DB/SQL.db"))
    DB.executeSQL('INSERT INTO disneyticket(date,TDL,TDS) values("{0}","{1}","{2}")'.format(date,infoTDL,infoTDS))

# if __name__ == '__main__':
#     DB = OriginalSQLLite3(dbname="./DB/SQL.db")
#     DB.executeSQL('CREATE TABLE IF NOT EXISTS disneyticket(id INTEGER PRIMARY KEY AUTOINCREMENT,date TEXT,TDL STRING,TDS STRING)')
#     DB.executeSQL('INSERT INTO disneyticket(date,TDL,TDS) values("2021-01-01","is_none","is_none")')
#     DB.fetchallSQL('SELECT * FROM disneyticket')