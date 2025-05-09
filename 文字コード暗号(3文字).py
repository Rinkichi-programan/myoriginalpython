hirabun=input("平文を入力してください-->") #input関数は、ユーザーに入力させる。
angobun="" #箱の準備
kagi=3

for moji in hirabun:
    angobun += chr(ord(moji)^kagi) #+kagiでも可

print(angobun)