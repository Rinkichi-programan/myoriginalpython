#乱数生成モジュールのインポート
import random

#起動メッセージ表示
print("じゃんけんゲーム version 1.00")
print("グー=0、チョキ=1、パー=2")

#ユーザーの勝敗数の初期化
win=0
lose=0

#5回勝負(あいこはノーカウント)⇒決まった数を繰り返すわけではないので、forではなくwhile
n=1
while n<=5:
    #ユーザーの手の入力
    print()
    user=int(input("ユーザーの手-->"))

    #コンピュータの手を乱数で決める
    computer=random.randint(0,2)
    print(f"コンピュータの手-->{computer}")

    #勝敗判定
    if user==computer:
        print("あいこです。")
    elif user==(computer-1)%3:
        print("ユーザーの勝ちです。")
        win +=1
        n +=1
    else:
        print("ユーザーの負けです。")
        lose +=1
        n +=1
    
    #結果発表～～～～～～！！！！！(浜田風)
    print(f"{win}勝{lose}敗です。")