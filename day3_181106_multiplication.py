a="Y"
while a=="y" or a=="Y":
    # input 받기
    num=int(input("What number of table do you want? "))
    #num이 숫자가 아니면?재요청
    if(num!=int()):
        num=int(input("type in number only"))
    else
        # i가 0~9인동안 출력
        for i in range(1,10):
            print("{} x {} = {}".format(num,i,num*i))
    # 지속 여부?
    a=input("Continue? (Y/N)")
pass
