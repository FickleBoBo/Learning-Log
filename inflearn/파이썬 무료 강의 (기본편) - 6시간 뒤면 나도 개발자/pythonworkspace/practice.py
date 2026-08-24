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

# 리스트
subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

print(subway.index("조세호"))

subway.append("하하")
print(subway)

subway.insert(1, "정형돈")
print(subway)

print(subway.pop())
print(subway)

subway.append("유재석")
print(subway)
print(subway.count("유재석"))

num_list = [5, 2, 4, 3, 1]
num_list.sort()
print(num_list)

num_list.reverse()
print(num_list)

num_list.clear()
print(num_list)

mix_list = ["조세호", 20, True]
print(mix_list)

num_list = [5, 2, 4, 3, 1]
mix_list = ["조세호", 20, True]
num_list.extend(mix_list)
print(num_list)

# 사전
cabinet = {3: "유재석", 100: "김태호"}
print(cabinet[3])
print(cabinet[100])
# print(cabinet[5])

print(cabinet.get(3))
print(cabinet.get(5))
print(cabinet.get(5, "사용 가능"))

print(3 in cabinet)
print(5 in cabinet)

cabinet = {"A-3": "유재석", "B-100": "김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

del cabinet["A-3"]
print(cabinet)

print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())

cabinet.clear()
print(cabinet)

# 튜플
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

(name, age, hobby) = "김종국", 20, "코딩"
print(name, age, hobby)

# 세트
my_set = {1, 2, 3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

print(java & python)
print(java.intersection(python))

print(java | python)
print(java.union(python))

print(java - python)
print(java.difference(python))

python.add("김태호")
print(python)

java.remove("김태호")
print(java)

# 자료구조의 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))

# if
# weather = input("오늘 날씨는 어때요? ")
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요")

# temp = int(input("기온은 어때요? "))
# if 30 <= temp:
#     print("너무 더워요. 나가지 마세요")
# elif 10 <= temp < 30:
#     print("괜찮은 날씨에요")
# elif 0 <= temp < 10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요. 나가지 마세요")

# for
for waiting_no in range(1, 6):
    print(f"대기번호 : {waiting_no}")

starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
    print(f"{customer}, 커피가 준비되었습니다.")

# while
customer = "토르"
index = 5
while index >= 1:
    print(f"{customer}, 커피가 준비 되었습니다. {index} 번 남았어요.")
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다.")

# customer = "아이언맨"
# index = 1
# while True:
#     print(f"{customer}, 커피가 준비 되었습니다. 호출 {index} 회")
#     index += 1

# customer = "토르"
# person = "Unknown"
# while person != customer:
#     print(f"{customer}, 커피가 준비 되었습니다.")
#     person = input("이름이 어떻게 되세요? ")

# continue 와 break
absent = [2, 5]
no_book = [7]
for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print(f"오늘 수업 여기까지. {student}는 교무실로 따라와")
        break
    print(f"{student}, 책을 읽어봐")


# 한 줄 for
students = [1, 2, 3, 4, 5]
print(students)
students = [i + 100 for i in students]
print(students)

students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)

students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)
