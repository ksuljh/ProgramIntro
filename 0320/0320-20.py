n = int(input("정수를 입력하시오: "))

result = 1

for i in range(n, 0, -1): 
    result = result * i

print(f"{n}! = {result}")