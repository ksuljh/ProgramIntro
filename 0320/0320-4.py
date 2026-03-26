import random

num1 = random.randint(1, 100)
num2 = random.randint(1, 100)

correct_answer = num1 + num2

print(f"{num1} + {num2} = ?")

user_answer = int(input("정답을 입력하세요: "))

if user_answer == correct_answer:
    print("True")
else:
    print("False")