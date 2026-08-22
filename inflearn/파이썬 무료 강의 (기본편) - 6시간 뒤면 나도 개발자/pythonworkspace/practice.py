# 숫자 자료형
print(5)
print(-10)
print(3.14)
print(1000)
print(5 + 3)
print(2 * 8)
print(3 * (3 + 1))

# 문자열 자료형
print("풍선")
print("ㅋㅋㅋㅋㅋㅋㅋㅋ")
print("ㅋ" * 8)

# boolean 자료형
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5 > 10))

# 변수
print("우리집 강아지의 이름은 연탄이에요")
print("연탄이는 4살이며, 산책을 아주 좋아해요")
print("연탄이는 어른일까요? True")

animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 " + name + "이에요")
print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
print(name + "는 어른일까요? " + str(is_adult))

# 주석
"""
이렇게
하면
여러문장이
주석처리
됩니다
"""

# 연산자
print(1 + 1)
print(3 - 2)
print(5 * 2)
print(6 / 3)

print(2**3)
print(5 % 3)
print(10 % 3)
print(5 // 3)
print(10 // 3)

print(10 > 3)
print(4 >= 7)
print(10 < 3)
print(5 <= 5)

print(3 == 3)
print(4 == 2)
print(3 + 4 == 7)

print(1 != 3)
print(not (1 != 3))

print((3 > 0) and (3 < 5))
print((3 > 0) & (3 < 5))

print((3 > 0) or (3 < 5))
print((3 > 0) | (3 < 5))

print(5 > 4 > 3)
print(5 > 4 > 7)

# 간단한수식
print(2 + 3 * 4)
print((2 + 3) * 4)

number = 2 + 3 * 4
print(number)
number = number + 2
print(number)
number += 2
print(number)
number *= 2
print(number)
number /= 2
print(number)
number -= 2
print(number)
number %= 5
print(number)

# 숫자처리함수
print(abs(-5))
print(pow(4, 2))
print(max(5, 12))
print(min(5, 12))
print(round(3.14))
print(round(4.99))

from math import *

print(floor(4.99))
print(ceil(3.14))
print(sqrt(16))

# 랜덤함수
from random import *

print(random())
print(random() * 10)
print(int(random() * 10))
print(int(random() * 10))
print(int(random() * 10))
print(int(random() * 10 + 1))
print(int(random() * 10 + 1))
print(int(random() * 10 + 1))
print(int(random() * 10 + 1))
print(int(random() * 10 + 1))
print(int(random() * 10 + 1))

print(int(random() * 45 + 1))
print(int(random() * 45 + 1))
print(int(random() * 45 + 1))
print(int(random() * 45 + 1))
print(int(random() * 45 + 1))
print(int(random() * 45 + 1))

print(randrange(1, 46))
print(randrange(1, 46))
print(randrange(1, 46))
print(randrange(1, 46))
print(randrange(1, 46))
print(randrange(1, 46))

print(randint(1, 45))
print(randint(1, 45))
print(randint(1, 45))
print(randint(1, 45))
print(randint(1, 45))
print(randint(1, 45))

# 문자열
sentence = "나는 소년입니다"
print(sentence)

sentence2 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence2)

# 슬라이싱
jumin = "990120-1234567"
print("성별 : " + jumin[7])
print("연 : " + jumin[0:2])
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[:6])
print("뒤 7자리 : " + jumin[7:])
print("뒤 7자리 (뒤에부터) : " + jumin[-7:])

# 문자열처리함수
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("n"))
print(python.find("Java"))
# print(python.index("Java"))
print(python.count("n"))

# 문자열포맷
print("나는 %d살입니다." % 20)
print("나는 %s를 좋아해요." % "파이썬")
print("Apple은 %c로 시작해요." % "A")
print("나는 %s살입니다." % 20)
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨간", age=20))

age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

# 탈출문자
print("백문이 불여일견\n백견이 불여일타")
print('저는 "나도코딩"입니다.')
print("\\")
print("Red Apple\rPine")
print("Redd\bApple")
print("Red\tApple")
