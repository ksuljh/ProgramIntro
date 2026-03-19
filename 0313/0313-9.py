# 목과 나머지 연산
p = 7
q = 4
print(f"나눗셈의 몫 = {p//q}")
print(f"나눗셈의 나머지 = {p % q}")

today = 0
print((today + 10) % 7)

# 할당 연산
x = y = z = 0
x,y,z = 10, 20, 30
x,y = y,x

# 복합 연산자
x = 1000
print(f"초깃값 x = {x}")
x +=2
print(f"x+= 후의 x = {x}")
x -=2
print(f"x-=2 후의 x= {x}")

# 지수 계산
a = 1000
r = 0.05
n = 10
result = a*(1+r)**n

print(f"원리금 합계 = {result}")