#파일 안의 단어 분석하기
from collections import Counter

f = open("C://programyaru.txt", encoding="utf-8")
count = Counter(f.read().split())
print("단어 출현 횟수 :", count)