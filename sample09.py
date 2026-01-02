# 必須モジュールの例
import os
import sys
import datetime

# 現在の作業ディレクトリを取得
print("現在のディレクトリ:", os.getcwd())

# コマンドライン引数を取得
print("コマンドライン引数:", sys.argv)

# 現在の日付と時刻を取得
print("現在の日付と時刻:", datetime.datetime.now())
