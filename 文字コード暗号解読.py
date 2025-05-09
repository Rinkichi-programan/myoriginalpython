bun1=input("暗号文を入力してください-->")
for kagi in range(0,10,1): #0~9の範囲での総当たり攻撃
    bun2=""
    for moji in bun1:
        bun2 += chr(ord(moji)^kagi) #^は、XOR演算
    print(f"鍵{kagi}:{bun2}")