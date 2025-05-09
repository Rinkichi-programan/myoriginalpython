import random

# グー=0、チョキ=1、パー=2とする。

# aを手動入力
try:
    a = int(input("あなたの手を入力してください (グー=0, チョキ=1, パー=2): "))
    print(a)
    if a not in [0, 1, 2]:
        raise ValueError("0, 1, 2のいずれかを入力してください。")
except ValueError as e:
    print(e)
    exit()

# bを乱数で選択
b = random.randint(0, 2)
print(f"相手の手: {b} (グー=0, チョキ=1, パー=2)")

# 勝敗判定
if a == b:
    print("あいこ")
elif (a + 1) % 3 == b:
    print("あなたの勝ち")
else:
    print("相手の勝ち")
    print("弱いね")