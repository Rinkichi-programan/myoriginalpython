#初期値(maxは鶴と亀の合計) 鶴がx匹、亀がy匹とする。
max=10
x=0

#鶴がmax匹以内の保証
while x<=10:
    y=0 #x固定、y初期化
    while y<=10:
        if (x+y==10) and (2*x+4*y==32):
            print(f"鶴={x}、亀={y}")
            x+=max
            y+=max #break処理と同義
        else:
            y+=1
    x+=1

#breakで実装するには、continueとかも使って、ちょっと工夫が必要だったような、、