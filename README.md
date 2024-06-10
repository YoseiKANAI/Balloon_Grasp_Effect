# Balloon_Grasp_Effect

風船把持効果の解析用プログラム  
測定結果を利用し，重心動揺解析と相互相関解析を行う  



  
## tsv_to_csv.py
計測したtsvファイルをcsvファイルに変換する  
Data/日付/sub〇/csvに保存  


## extract_COP.py  
tsv_to_csvで作成したcsvファイルのうち，f_1とf_2からCOPを抜き出し，COPディレクトリに保存  
Data/日付/sub〇/csv/COPに保存  


## replarce_fp.py  
フォースプレートデータの２つを一つにまとめるプログラム「ForcePlateIndex_f」のためにデータを整形する  
Data/日付/sub〇/csv/fpにデータを保存  

## ForcePlateIndex_f

２つのフォースプレートのデータを一つにまとめる  
出力　Data/日付に保存  
dump：２つのデータをまとめたCOPとZ方向の反力を記載したデータ  
各タスクの試行ごとに保存されている  

result：すべての指標を算出した結果を出力  
被験者ごとに出力  

## cal_means.py  
フォースプレートのリザルトを使用  
各被験者のタスクごとに試行回数で平均をとる  
グラフのプロットも行う  

## create_CCA_data.py  
CCA（相互相関解析）のためにデータを整形，ディレクトリを移す  
（filteredは中にサビスキーフィルタも含まれているやつ）  

## savizky_golay.py  
サビスキーゴーレイフィルタを使用できるfunc関数が格納されている  

## cal_Force.py  
指先に加わる力覚を導出  
式はpaper19-20参照  

## CAA_COP_Force.py  
目的変数：F（力覚）  
説明変数：COP  

利用するためにはCCA内部に２つディレクトリを作成して，そこに力覚とCOPを保存する．  
- 算出値  
    指先が動いてから何ms後にCOPが変化したか（Lag）  
    指先とCOPの相関の確認  
    相関は正の値のほうが大きくなっている  
    

## CAA_OBject_hand.py  
 
目的変数：指先座標  

説明変数：物体座標  
