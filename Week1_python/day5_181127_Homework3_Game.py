# 과제 3 - 가위 / 바위 / 보 게임

## 가위바위보 해주는 함수
def judge(user):
    ## 컴퓨터도 무언가 내봅니다.
    import random as rd
    com=rd.choice(("Rock", "Scissor", "Paper") )

    ## 가위바위보 규칙을 컴에게 알려줍니다.
    if user=="Rock" or user=="rock":
        if com=="Rock":
            result="Tie"
        elif com=="Scissor":
            result="Win"
        else: result="Lose"
        pass
    elif user=="Scissor" or user=="scissor":
        if com=="Rock":
            result="Lose"
        elif com=="Scissor":
            result="Tie"
        else: result="Win"
        pass
    else :
        if com=="Rock":
            result="Win"
        elif com=="Scissor":
            result="Lose"
        else: result="Tie"
        pass
    pass
    return result


Game=("Rock","Scissor","Paper","rock","scissor","paper")
score_com=0
score_user=0

## 사용자에게 가위, 바위, 보 中 하나를 물어봅니다.
while score_com <3 and score_user <3:
    user=input("Rock, scissor, paper, Shoot!")
    if user not in Game:
        score_com=score_com
    else :
        result=judge(user)
        if result == "Win":
            score_user=score_user+1
        elif result=="Lose":
            score_com=score_com+1
        else:
            pass
        print("Result is {}".format(result))
        pass

print("The Final score of User vs Com is {} : {}".format(score_user,score_com))
