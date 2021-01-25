#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import time

import tkinter as tk
from tkinter.font import Font
import tkinter.ttk as ttk

import webscraping as websc
import DB_SQLlite as sql3

class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        master.title("ディズニー販売速報")
        # ウィンドウサイズを指定
        master.geometry("400x550")
        # master.state('zoomed')
        # ウィンドウサイズの変更可否設定
        master.resizable(1, 1)
        # ウィンドウの背景色
        master.configure(bg="white")

        # Tkinter Bugの対象用の関数
        # self.fix(master)

        # 表示するコンポーネント群の定義
        self.create_menubar(master)
        self.wrpFrm(master)
        self.Infomation_view()
        self.style_setting()
        self.create_operation_button()
        self.log_check_area()

    def style_setting(self):
        # スタイルの設定
        style = ttk.Style()
        # TreeViewの全部に対して、フォントサイズの変更
        style.configure("Treeview", font=("", 12))
        # TreeViewのHeading部分に対して、フォントサイズの変更と太字の設定
        style.configure("Treeview.Heading", font=("", 14, "bold"))

    # ラッパーフレーム
    def wrpFrm(self,master):
        self._wrpFrme = tk.Frame(master)
        self._wrpFrme.configure(bg="white")
        self._wrpFrme.pack(padx=3, pady=3, fill="both", expand=1)

    # データ表示するテーブル
    def Infomation_view(self):
        # imgList = ttk.Treeview(self._wrpFrme)
        columns = ("column1", "column2", "column3")
        imgList= ttk.Treeview(self._wrpFrme, columns=columns)
        imgList.column("#0", width=50)
        imgList.column("column1", width=100)
        imgList.column("column2", width=120)
        imgList.column("column3", width=120)
        imgList.pack()
        imgList.heading("#0", text="No")
        imgList.heading("column1", text="日付")
        imgList.heading("column2", text="TDL Status")
        imgList.heading("column3", text="TDS Status")
        self.imgList = imgList

    # メニューバー作成
    def create_menubar(self,master):
        # menubarの大元（コンテナ）の作成と設置
        _menubar = tk.Menu(master)
        master.config(menu=_menubar)
        # menubarを親として設定メニューを作成と表示
        setting_menu = tk.Menu(_menubar, tearoff=0)
        _menubar.add_cascade(label='設定', menu=setting_menu)
        # menubarを親としてヘルプメニューを作成と表示
        help_menu = tk.Menu(_menubar, tearoff=0)
        _menubar.add_cascade(label='ヘルプ', menu=help_menu)

    # 異本的な操作をするボタンの配置
    def create_operation_button(self):
        # グリッド用のFrame
        confGridFrm = tk.Frame(self._wrpFrme)
        confGridFrm.configure(bg="white")
        confGridFrm.pack(padx=3, pady=3, fill="x")

        # ネームルールフレーム
        basicallyfrm = tk.LabelFrame(confGridFrm)
        basicallyfrm.configure(bg="white", text="基本的な動作", relief="groove",foreground = 'red')
        basicallyfrm.pack(padx=3, pady=3)

        # 情報取得用のボタン
        getData = tk.Button(basicallyfrm)
        getData.configure(background="#ff7f50",foreground='red',text="データを取得",command=self.getData_click)
        getData.pack(side="left", padx=5)

        # 画像撮影ボタン
        takePictureBtn = tk.Button(basicallyfrm,background="red")
        takePictureBtn.configure(text="画像を撮影",foreground = 'red',command=self.takePicture_click)
        takePictureBtn.pack(side="left", padx=5)

    # 実行状況の確認用のテキストエリア表示
    def log_check_area(self):
        # グリッド用のFrame
        Log_confirmation = tk.Frame(self._wrpFrme,relief='sunken')
        Log_confirmation.pack(padx=3, pady=3, fill="x")

        # ネームルールフレーム
        Log_confirmation_frame = tk.LabelFrame(Log_confirmation)
        Log_confirmation_frame.configure(bg="white", text="ログ出力", relief="groove", foreground='red')
        Log_confirmation_frame.pack(padx=3, pady=3,fill="x")

        # 表示するだけのテキストエリア
        self.log_display_area = tk.Text(Log_confirmation_frame, height=10,width=50)
        self.log_display_area.grid(row=1, column=0, sticky=(tk.N, tk.W, tk.S, tk.E))
        self.log_print_area("アプリケーション起動")

    # ログ出力エリアの制御部分
    def log_print_area(self,display_text=""):
        self.log_display_area.configure(state=tk.NORMAL)
        dt_now = datetime.datetime.now()
        row = self.log_display_area.index('end')
        self.log_display_area.insert(float(row), "{0} > {1}\n".format(dt_now.strftime('%Y%m%d %H:%M:%S'),display_text))
        self.log_display_area.configure(state=tk.DISABLED)

    # 情報取得用のボタンが押された時の処理
    def getData_click(self):
        # データベース初期化
        self.log_print_area("内部のデータベース初期化")
        sql3.desney_data_chiket_Initialize()

        datas = websc.ticket_scraping_main()
        for i,data in enumerate(datas):
            # 完売情報の表示置き換え処理
            infoTDL = ('完売' if data["TDL"] == 'is-none' else '販売中止' if data["TDL"] == 'is-close' else '販売中')
            infoTDS = ('完売' if data["TDS"] == 'is-none' else '販売中止' if data["TDS"] == 'is-close' else '販売中')

            # 販売情報に対するboolean情報Flag
            flagTDL = (False if data["TDL"] == 'is-none' else False if data["TDL"] == 'is-close' else True)
            flagTDS = (False if data["TDS"] == 'is-none' else False if data["TDS"] == 'is-close' else True)
            judgeFlag = flagTDL or flagTDS
            mappingKey = ('Yes' if judgeFlag == True else 'No')

            # GUI クライアントのテーブルに情報を挿入
            self.imgList.insert("", "end", text=i, values=(data["date"], infoTDL, infoTDS),tags=(mappingKey,))
            sql3.desney_data_chiket_Incert(data["date"], data["TDL"].replace("is-",""), data["TDS"].replace("is-",""))
        self.log_print_area("内部のデータベースへの情報保存")
        # 販売していない場合のカラー処理
        self.imgList.tag_configure('No', background="red",foreground="white")
        self.log_print_area("スクレイピング実行完了")

    # インスタ用の写真撮影の処理
    def takePicture_click(self):
        print("写真撮影")


def main():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()