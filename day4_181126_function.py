 # 리스트, 튜플에서 랜덤뽑기 도전
import NumPy
num=[1,2,3,4,5]

# #1~5까지 숫자중 하나를 선택
# choose=random.choice(5,2,replace=False)
# print(choose)

#1~9까지 정수중 하나 선택
choose2=random.randint(0,10)
print(choose2)

#0~1까지 float중 리턴
choose3=random.random()
print(choose3)

#11~100 중 난수선택
choose4=random.randrange(11,100)
print(choose4)

#num에서 2개 골라서 생성
choose5=random.sample(num,2)
print(choose5)
