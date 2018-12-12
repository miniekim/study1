# 과제 5- 에러나지않는 구구단

#구구단 함수
def multiply ():
    try:
        user=int(input("Type in number between 2~9 :"))
        if user < 10 and user > 1:
            for i in range(1,10):
                print("{}x{}={}".format(user,i,user*i))
        else:
            print("only 2~9 is allowed. ")
            multiply()

    except ValueError:
        print("Only Numbers")
        multiply()

    except:
        print("Error has been occured")
        muliply()


multiply()
