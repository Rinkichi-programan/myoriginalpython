# グー=0、チョキ=1、パー=2とする。
a=1
b=2

#a=bならあいこ、a+1を3で割った余りがbならAの勝ち、それ以外はBの勝ち
if a==b:
    print("あいこ")
elif (a+1)%3==b:
    print("Aの勝ち")
else:
    print("Bの勝ち")

#いつかはn人(n>=3)じゃんけんを実装してみたい。