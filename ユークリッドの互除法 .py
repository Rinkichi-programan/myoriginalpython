# aとbの最大公約数を求める。
a=12
b=42

#a=bになるまで繰り返す。最後にa(bでも可)をプリント
while a!=b:
    if a>b:
        a-=b
    else:
        b-=a
print(f"最大公約数は{a}です。")

#ユーザー定義関数で、gcd関数とかを実装してみる。gcd(a,b) 使い方はprint(gcd(a,b))