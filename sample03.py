# 数当てゲーム
import random

number = random.randint(1, 100)
tries = 0
guess = 0

print("1から100までの数を当ててください")

while guess != number:
    guess = int(input("あなたの推測は？ "))
    tries += 1
    if guess < number:
        print("もっと大きいです")
    elif guess > number:
        print("もっと小さいです")

print(f"おめでとうございます！ {tries}回で当たりました")
