def conti():
    a=input("Would you try again?(y/n) ")
    if (a!="y" and a!="Y" and a!="n" and a!="N"):
        print("Invalid.Only Y/N")
        return conti()
    else : return a


Chinese=("Mr.hong","chinachina","china-jeong","Black noodle")
Japanese=("Raman","shu-shi","Sasimi","tuna plate")
Korean=("steamed cow","pork belly","beef delcious")

#한식, 중식, 일식 중 한가지를 고르라고 한다!

cont="y"
while cont=="y" or cont=="Y":
    preference=int(input("Choose among 1.Korean, 2.Japanese, 3.Chinese food! Type in 1 or 2 or 3. "))
    import random as rd
    if preference==1:
        print(rd.choice(Chinese))
        cont=conti()

    elif preference==2:
        print(rd.choice(Japanese))
        cont=conti()

    elif preference==3:
        print(rd.choice(Korean))
        cont=conti()

    else : print("Invalid")
    pass
