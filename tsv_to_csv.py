# %%
# -*- coding: utf-8 -*-

import os
import csv

# 被験者数を指定
subnum = 5

for ID in range(subnum):
    # ルートフォルダ(Dataフォルダ)のパスを指定
    root_dir = "D:/User/kanai/Data/test/sub%d" %(ID+1)
    # 出力先フォルダを作成
    output_dir = os.path.join(root_dir, "csv")
    os.makedirs(output_dir, exist_ok=True)

    # ルートフォルダ以下のすべてのフォルダに対して処理を実行
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # フォルダ内のすべてのcsvファイルに対して処理を実行
        for filename in filenames:
            # tsvファイルならTrue
            if filename.endswith(".tsv"):
                # tSVファイルのパスを作成
                input_path = os.path.join(dirpath, filename)
                # 出力ファイル名(csvファイル名)を指定
                output_filename = filename.replace("tsv", "csv")
                output_path = os.path.join(output_dir, output_filename)

                # TSVファイルを開く
                with open(input_path, encoding='utf-8', newline='') as input_file:
                    tsv = csv.reader(input_file, delimiter = '\t')

                    # 出力ファイルを開く
                    with open(output_path, "w", newline='') as output_file:
                        writer = csv.writer(output_file, delimiter=",")
                        i = 0
                        # 出力ファイルに書き込み
                        # 各型式で上部の余分なデータを除く処理を行う
                        for row in tsv:
                            if (filename.endswith("_2D.tsv")):
                                if (i>6):
                                    writer.writerow(row)
                                else:
                                    i = i + 1
                            elif (filename.endswith("_a.tsv")):
                                if (i>12):
                                    writer.writerow(row)
                                else:
                                    i = i + 1
                            elif (filename.endswith(("f_1.tsv", "f_2.tsv"))):
                                if (i>25):
                                    writer.writerow(row)
                                else:
                                    i = i + 1
                            else:
                                if (i>10):
                                    writer.writerow(row)
                                else:
                                    i = i + 1            
                        output_file.close()
                    input_file.close()
        # カレントディレクトリの走査が終わったら終了
        break