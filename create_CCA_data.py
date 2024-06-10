# %%
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 14:55:23 2023

@author: ShimaLab
"""

import os
import csv
import pandas as pd
from . import savitzky_golay

# 被験者数を指定
subnum = 1


# COP入力パス（dump）
root_input_COP = "D:/User/kanai/Data/240601/result_COP/dump"

# dumpファイルと力覚を同じディレクトリに移動する
for i in range(subnum):
    # ルートフォルダのパスを指定（力覚データの格納場所）
    root_dir = "D:/User/kanai/Data/240601/sub%d/csv" % (i+1)
    
    # 出力先フォルダを作成
    output_dir_Force = os.path.join(root_dir, "Force_ori")
    os.makedirs(output_dir_Force, exist_ok=True)
    
    # 出力先フォルダを作成
    output_dir_COP = os.path.join(root_dir, "COP_ori")
    os.makedirs(output_dir_COP, exist_ok=True)

    # 力覚
    # ルートフォルダ以下のすべてのフォルダに対して処理を実行
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # フォルダ内のすべてのcsvファイルに対して処理を実行
        for filename in filenames:
            if filename.endswith(("f_1.csv", "f_2.csv","_2D.csv", "_a.csv")):
                continue
            if filename.startswith(("NC", "WG")):
                continue            
            if filename.endswith((".csv")):
                # CSVファイルのパスを作成
                input_path = os.path.join(dirpath, filename)

                # 出力ファイル名を作成
                output_filename = filename
                output_filename = output_filename.replace("00", "")
                output_path_Force = os.path.join(output_dir_Force, output_filename)

                # CSVファイルを開く
                with open(input_path, "r") as input_file:
                    reader = csv.reader(input_file)

                    # 出力ファイルを開く
                    with open(output_path_Force, "w", newline="") as output_file:
                        writer = csv.writer(output_file)

                        # 出力ファイルに力覚データを書き込む
                        for row in reader:
                            output_row = [row[2], row[3], row[4], row[5], row[6], row[7]]
                            writer.writerow(output_row)
        # カレントディレクトリの走査が終わったら終了
        break
    
    # COP
    # ルートフォルダ以下のすべてのフォルダに対して処理を実行
    for dirpath, dirnames, filenames in os.walk(root_input_COP):
        # フォルダ内のすべてのcsvファイルに対して処理を実行
        for filename in filenames:
            if filename.endswith((".csv")):
                # CSVファイルのパスを作成
                input_path = os.path.join(dirpath, filename)

                # 出力ファイル名を作成
                output_filename = filename
                output_path_Force = os.path.join(output_dir_COP, output_filename)
    
                # CSVファイルを開く
                with open(input_path, "r") as input_file:
                    reader = csv.reader(input_file)

                    # ヘッダーをスキップ
                    next(reader)

                    # 出力ファイルを開く
                    with open(output_path_Force, "w", newline="") as output_file:
                        writer = csv.writer(output_file)
                        # ヘッダーを出力
                        writer.writerow(["COP_X", "COP_Y"])
                        i = 0
                        for row in reader:
                            output_row = [row[0], row[1]]
                            writer.writerow(output_row)
        # カレントディレクトリの走査が終わったら終了
        break
    """
    データ数を合わせる場合
                        # 出力ファイルにCOPデータを書き込む
                        # フォースプレート：1kHz
                        # モーキャプ：0.1kHz
                        # サンプリングを合わせるため10刻みで記入
                        for row in reader:
                            if ((i+1)%10 == 1):
                                output_row = [row[0], row[1]]
                                writer.writerow(output_row)
                                i = i+1
                            else:
                                i = i+1
    
    """