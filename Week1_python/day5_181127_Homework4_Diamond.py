# 과제4_다이아몬드 그리기!

list=[-2,-1,0,1,2]

for i in list:
    for j in list:
        if(i*j<-1 or i*j>1):
            print(0,end='')
        else:
            print(1,end='')
        pass
    pass
    print('')
pass
