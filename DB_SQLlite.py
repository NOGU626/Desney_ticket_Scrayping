#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3

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

if __name__ == '__main__':
    DB = OriginalSQLLite3(dbname="SQL.db")
    # DB.executeSQL('CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT,name STRING)')
    DB.executeSQL('INSERT INTO persons(name) values("Taro")')
    DB.fetchallSQL('SELECT * FROM persons')