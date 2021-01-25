#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk
import tkinter.ttk as ttk

if __name__ == "__main__":
	root = tk.Tk()
	root.title("Image editing app")
	# ウィンドウサイズを指定
	root.geometry("400x550")
	# ウィンドウサイズの変更可否設定
	root.resizable(0, 0)
	# ウィンドウの背景色
	root.configure(bg="white")

	# ラッパーフレーム
	wrpFrm = tk.Frame(root)
	wrpFrm.configure(bg="white")
	wrpFrm.pack(padx=3, pady=3, fill="both", expand=1)

	# 読み込んだ画像リスト
	imgList = ttk.Treeview(wrpFrm)
	imgList.configure(column=(1, 2), show="headings", height=6)
	imgList.column(1, width=30)
	imgList.column(2, width=361)
	imgList.heading(1, text="No")
	imgList.heading(2, text="path/name")
	imgList.pack()

	# ボタン中央揃え用のフレーム
	btnFrm = tk.Frame(wrpFrm)
	btnFrm.configure(bg="white")
	btnFrm.pack(pady=5)

	# 画像追加ボタン
	addBtn = tk.Button(btnFrm)
	addBtn.configure(text="add")
	addBtn.pack(side="left", padx=5)

	# 画像リセットボタン
	resetBtn = tk.Button(btnFrm)
	resetBtn.configure(text="画像をリセット")
	resetBtn.pack(side="left", padx=5)

	# グリッド用のFrame
	confGridFrm = tk.Frame(wrpFrm)
	confGridFrm.configure(bg="white")
	confGridFrm.pack(padx=3, pady=3, fill="x")

	# ネームルールフレーム
	renameFrm0 = tk.LabelFrame(confGridFrm)
	renameFrm0.configure(bg="white", text="リネームルール", relief="groove")
	renameFrm0.grid(row=0, column=1, pady=(0, 5))

	# 画像追加ボタン
	addBtn0 = tk.Button(renameFrm0)
	addBtn0.configure(text="add")
	addBtn0.pack(side="left", padx=5)

	# 画像リセットボタン
	resetBtn0 = tk.Button(renameFrm0)
	resetBtn0.configure(text="画像をリセット")
	resetBtn0.pack(side="left", padx=5)

	# ネームルールフレーム
	renameFrm = tk.LabelFrame(confGridFrm)
	renameFrm.configure(bg="white", text="リネームルール", relief="groove")
	renameFrm.grid(row=0, column=0, pady=(0, 5))

	# 画像追加ボタン
	addBtn1 = tk.Button(renameFrm)
	addBtn1.configure(text="add")
	addBtn1.pack(side="left", padx=5)

	# 画像リセットボタン
	resetBtn1 = tk.Button(renameFrm)
	resetBtn1.configure(text="画像をリセット")
	resetBtn1.pack(side="left", padx=5)

	root.mainloop()
