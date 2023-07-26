"""문장 하나가 아니라
문단 단위의 주석이 필요할 때

from random import randint, uniform

user_num = int(input("Choose a number."))

answer = randint(1, 99)

if user_num == answer:
    print("You win!!!")
elif user_num > answer:
    print("Go lower! The answer was", answer)
else:
    print("Go higher! The answer was", answer)"""

distance = 0

while distance <= 20:
    print("ghhhhh", distance, "km... tough stuff")
    distance = distance + 1
