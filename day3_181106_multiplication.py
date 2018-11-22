a="Y"
while a=="y" or a=="Y":
    # input 받기
    num=int(input("What number of table do you want?(2~9 only)"))
    # 2~9사이 값이 아닌경우, 재요청
    while num<2 or num>9:
        print("2~9 only")
        num=int(input("What number of table do you want?(2~9 only)"))
    pass

    # i가 0~9인동안 출력
    for i in range(1,10):
            print("{} x {} = {}".format(num,i,num*i))
    # 지속 여부?
    a=input("Continue? (Y/N)")
    while a!="n" and a!="N" and a!="y" and a!="Y" :
        a=input("Continue? (Y/N)")
    pass
pass
