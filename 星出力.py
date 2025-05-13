cnt=0
num=5
starColor="SC1"
while cnt<num:
    if starColor=="SC1":
        print("☆",end=" ")
        starColor="SC2"
    else:
        print("★",end=" ")
        starColor="SC1"
    cnt +=1
print()