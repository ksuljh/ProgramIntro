#문제 3

ObjectPrice = int(input("물건값을 입력하시오 : "))
OneThousandWonCount = int(input("1000원 : "))
FiveHundredWonCount = int(input("500원 : "))
OneHundredWonCount = int(input("100원 : "))

OneThousandWon = OneThousandWonCount * 1000
FiveHundredWon = FiveHundredWonCount * 500
OneHundredWon = OneHundredWonCount * 100

TotalPrice = OneThousandWon + OneHundredWon + FiveHundredWon
print(f"총 값은 : {TotalPrice}원 입니다.")

BuyCount = TotalPrice // ObjectPrice
ResultPrice = TotalPrice % ObjectPrice
print(f"물건을 {BuyCount}개 구매하셨습니다.")

RemainOT = ResultPrice % 1000
ResultOT = ResultPrice // 1000
print(f"1000원 개수 : {ResultOT}")
RemainFH = RemainOT % 500
ResultFH = RemainOT // 500
print(f"500원의 개수 : {ResultFH}")
RemainOH = RemainFH % 100
ResultOH = RemainFH // 100
print(f"100원의 개수 : {ResultOH}")
RemainTenWon = RemainOH % 10
ResultTenWon = RemainOH // 10
print(f"10원의 개수 : {ResultTenWon}")
RemainOneWon = RemainTenWon % 1
ResultOneWon = RemainTenWon // 1
print(f"1원의 개수 : {ResultOneWon}")