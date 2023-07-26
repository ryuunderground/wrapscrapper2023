from random import randint
# 업다운 게임 만들기
print("Welcome to Pythin Up-Down")
answer = randint(1, 99)

playing = True
challenge = 1
while playing:
    user_num = int(input("Name a number."))
    if user_num == answer:
        print("You win!!! Congrats! Succeed in", challenge, "tries")
        playing = False
    elif user_num > answer:
        print("Go lower!")
        challenge = challenge + 1
    else:
        print("Go higher!")
        challenge = challenge + 1
