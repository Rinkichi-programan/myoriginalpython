#初期値
a=91
ans="素数です"
n=2
n_max=a-1

#2~a-1まで評価する
while n<=n_max:
    if a%n==0:
        ans="素数ではありません。"
        break
    else: #elseは省略可
        n +=1

print(f"{a}は{ans}")

#余談：n_maxを、aの半分や、aの平方根にすると処理時間を短縮できる。
