# メモアプリ
memo = []

while True:
    command = input("1: メモ追加, 2: メモ表示, 3: 終了 >> ")
    if command == '1':
        memo.append(input("メモ: "))
    elif command == '2':
        for idx, note in enumerate(memo):
            print(f"{idx + 1}: {note}")
    elif command == '3':
        break
    else:
        print("無効なコマンドです")
