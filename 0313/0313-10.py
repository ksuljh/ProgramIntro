# 복리 계산

InitMoney = 24
Interset = 0.06
Years = 382
print(InitMoney*(1+Interset)**Years)

# 반올림
price = 12345
tax = price * 0.075
tax = round(tax,2)
print(tax)

# 큰 따옴표 사용
msg = "Hello"
print(msg)

message = "철수가 '안녕'이라고 말했습니다. "
print(message)

a = """TWINLEKRJWL
WLERJ
lwelr"""

print(a)

lines = "-" * 30
print(lines)

# 숫자와 문자열의 구별

print(100+200)
print("100"+"200")

#movie = "Terminator" + 3

movie =  "Terminator" + str(3)
print(movie)

price = int("100")
Pl = float("3.14")

print("말 한마디로\n 천냥빚을 갚는다")