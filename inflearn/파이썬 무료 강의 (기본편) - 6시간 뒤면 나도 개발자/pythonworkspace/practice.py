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


# 함수
def open_account():
    print("새로운 계좌가 생성되었습니다.")


open_account()


# 전달값과 반환값
def deposit(balance, money):
    print(f"입금이 완료되었습니다. 잔액은 {balance + money} 원 입니다.")
    return balance + money


balance = 0
balance = deposit(balance, 1000)
print(balance)


def withdraw(balance, money):
    if balance >= money:
        print(f"출금이 완료되었습니다. 잔액은 {balance - money} 원 입니다.")
        return balance - money
    else:
        print(f"출금이 완료되지 않았습니다. 잔액은 {balance} 원 입니다.")
        return balance


balance = 0
balance = deposit(balance, 1000)
balance = withdraw(balance, 2000)
print(balance)


def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money - commission


commission, balance = withdraw_night(balance, 500)
print(f"수수료는 {commission} 원이며, 잔액은 {balance} 원 입니다.")


# 기본값
def profile(name, age, main_lang):
    print(f"이름 : {name}\t나이 : {age}\t주 사용 언어 : {main_lang}")


profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")


def profile(name, age=17, main_lang="파이썬"):
    print(f"이름 : {name}\t나이 : {age}\t주 사용 언어 : {main_lang}")


profile("유재석")
profile("김태호")


# 키워드값
def profile(name, age, main_lang):
    print(name, age, main_lang)


profile(name="유재석", main_lang="파이썬", age=20)
profile(main_lang="자바", age=25, name="김태호")


# 가변인자
def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print(f"이름 : {name}\t나이 : {age}\t", end=" ")
    print(lang1, lang2, lang3, lang4, lang5)


profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
profile("김태호", 25, "Kotlin", "Swift", "", "", "")


def profile(name, age, *language):
    print(f"이름 : {name}\t나이 : {age}\t", end=" ")
    for lang in language:
        print(lang, end=" ")
    print()


profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile("김태호", 25, "Kotlin", "Swift")

# 지역변수와 전역변수
gun = 10


# def checkpoint(soldiers):
#     gun = 20
#     gun = gun - soldiers
#     print(f"[함수 내] 남은 총 : {gun}")


# def checkpoint(soldiers):
#     global gun
#     gun = gun - soldiers
#     print(f"[함수 내] 남은 총 : {gun}")


def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print(f"[함수 내] 남은 총 : {gun}")
    return gun


print(f"전체 총 : {gun}")
# checkpoint(2)
gun = checkpoint_ret(gun, 2)
print(f"남은 총 : {gun}")

# 표준입출력
print("Python", "Java", "JavaScript", sep=" vs ")
print("Python", "Java", "JavaScript", sep=",", end="?")

import sys

print("Python", "Java", file=sys.stdout)
print("Python", "Java", file=sys.stderr)

scores = {"수학": 0, "영어": 50, "코딩": 100}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")

for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))

# answer = input("아무 값이나 입력하세요 : ")
# print(type(answer))
# print("입력하신 값은 " + answer + "입니다.")

# 다양한 출력포맷
print(f"{500:>10}")
print(f"{500:>+10}")
print(f"{-500:>+10}")
print(f"{500:_<+10}")
print(f"{100000000000:,}")
print(f"{100000000000:+,}")
print(f"{-100000000000:+,}")
print(f"{100000000000:^<+30,}")
print(f"{5 / 3:f}")
print(f"{5 / 3:.2f}")

# 파일입출력
# score_file = open("score.txt", "w", encoding="utf-8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf-8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf-8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf-8")
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf-8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line)
# score_file.close()

score_file = open("score.txt", "r", encoding="utf-8")
lines = score_file.readlines()
for line in lines:
    print(line, end="")
score_file.close()

# pickle
import pickle

# profile_file = open("profile.pickle", "wb")
# profile = {"이름": "박명수", "나이": 30, "취미": ["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file)
# profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)
print(profile)
profile_file.close()

# with
import pickle

with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf-8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요.")

with open("study.txt", "r", encoding="utf-8") as study_file:
    print(study_file.read())

# 섹션 9. 클래스
# name = "마린"
# hp = 40
# damage = 5

# print(f"{name} 유닛이 생성되었습니다.")
# print(f"체력 {hp}, 공격력 {damage}")

# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# tank2_name = "탱크"
# tank2_hp = 150
# tank2_damage = 35

# print(f"{tank_name} 유닛이 생성되었습니다.")
# print(f"체력 {tank_hp}, 공격력 {tank_damage}")


# def attack(name, location, damage):
#     print(f"{name} : {location} 방향으로 적군을 공격 합니다. [공격력 {damage}]")


# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# attack(tank2_name, "1시", tank2_damage)


# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print(f"{self.name} 유닛이 생성되었습니다.")
#         print(f"체력 {self.hp}, 공격력 {self.damage}")


# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

# wraith1 = Unit("레이스", 80, 5)
# print(f"유닛 이름 : {wraith1.name}, 공격력 : {wraith1.damage}")

# wraith2 = Unit("빼앗은 레이스", 80, 5)
# wraith2.clocking = True

# if wraith2.clocking == True:
#     print(f"{wraith2.name} 는 현재 클로킹 상태입니다.")


# class AttackUnit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage

#     def attack(self, location):
#         print(
#             f"{self.name} : {location} 방향으로 적군을 공격 합니다. [공격력 {self.damage}]"
#         )

#     def damaged(self, damage):
#         print(f"{self.name} : {damage} 데이지를 입었습니다.")
#         self.hp -= damage
#         print(f"{self.name} : 현재 체력은 {self.hp} 입니다.")
#         if self.hp <= 0:
#             print(f"{self.name} : 파괴되었습니다.")


# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# firebat1.damaged(25)
# firebat1.damaged(25)


# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed

#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print(f"{self.name} : {location} 방향으로 이동합니다. [속도 {self.speed}]")


# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage

#     def attack(self, location):
#         print(
#             f"{self.name} : {location} 방향으로 적군을 공격 합니다. [공격력 {self.damage}]"
#         )

#     def damaged(self, damage):
#         print(f"{self.name} : {damage} 데미지를 입었습니다.")
#         self.hp -= damage
#         print(f"{self.name} : 현재 체력은 {self.hp} 입니다.")
#         if self.hp <= 0:
#             print(f"{self.name} : 파괴되었습니다.")


# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# firebat1.damaged(25)
# firebat1.damaged(25)


# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print(f"{name} : {location} 방향으로 날아갑니다. [속도 {self.flying_speed}]")


# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage)
#         Flyable.__init__(self, flying_speed)

#     def move(self, location):
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)


# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")

# vulture = AttackUnit("벌쳐", 80, 10, 20)
# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시")
# # battlecruiser.fly(battlecruiser.name, "9시")
# battlecruiser.move("9시")


# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         # Unit.__init__(self, name, hp, 0)
#         super().__init__(name, hp, 0)
#         self.location = location


# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")


# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")


# def game_over():
#     pass


# game_start()
# game_over()


class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print(f"{name} 유닛이 생성되었습니다.")

    def move(self, location):
        print(f"{self.name} : {location} 방향으로 이동합니다. [속도 {self.speed}]")

    def damaged(self, damage):
        print(f"{self.name} : {damage} 데미지를 입었습니다.")
        self.hp -= damage
        print(f"{self.name} : 현재 체력은 {self.hp} 입니다.")
        if self.hp <= 0:
            print(f"{self.name} : 파괴되었습니다.")


class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print(
            f"{self.name} : {location} 방향으로 적군을 공격 합니다. [공격력 {self.damage}]"
        )


class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print(f"{name} : {location} 방향으로 날아갑니다. [속도 {self.flying_speed}]")


class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        self.fly(self.name, location)


class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print(f"{self.name} : 스팀팩을 사용합니다. (HP 10 감소)")
        else:
            print(f"{self.name} : 체력이 부족하여 스팀팩을 사용하지 않습니다.")


class Tank(AttackUnit):
    seize_developed = False

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return

        if self.seize_mode == False:
            print(f"{self.name} : 시즈모드로 전환합니다.")
            self.damage *= 2
            self.seize_mode = True
        else:
            print(f"{self.name} : 시즈모드를 해제합니다.")
            self.damage /= 2
            self.seize_mode = False


class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False

    def clocking(self):
        if self.clocked == True:
            print(f"{self.name} : 클로킹 모드를 해제합니다.")
            self.clocked = False
        else:
            print(f"{self.name} : 클로킹 모드를 설정합니다.")
            self.clocked = True


def game_start():
    print("[알림] 새로운 게임을 시작합니다.")


def game_over():
    print("Player : gg")
    print("[Player] 님이 게임에서 퇴장하셨습니다.")


game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

for unit in attack_units:
    unit.move("1시")

Tank.seize_developed = True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

for unit in attack_units:
    unit.attack("1시")

for unit in attack_units:
    unit.damaged(randint(5, 21))

game_over()

# 섹션 10. 예외처리
# try:
#     print("나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("첫 번째 숫자를 입력하세요 : "))
#     print(f"{num1} / {num2} = {int(num1 / num2)}")
# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err:
#     print(err)
# except:
#     print("알 수 없는 에러가 발생하였습니다.")

# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("첫 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise ValueError
#     print(f"{num1} / {num2} = {int(num1 / num2)}")
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")


# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg = msg

#     def __str__(self):
#         return self.msg


# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("첫 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError(f"입력값 : {num1}, {num2}")
#     print(f"{num1} / {num2} = {int(num1 / num2)}")
# except BigNumberError as err:
#     print(err)
# finally:
#     print("계산기를 이용해 주셔서 감사합니다.")

# 섹션 11. 모듈과 패키지
# import theater_module

# theater_module.price(3)
# theater_module.price_morning(4)
# theater_module.price_soldier(5)

# import theater_module as mv

# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import *

# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price, price_morning

# price(3)
# price_morning(4)

# from theater_module import price_soldier as price

# price(3)

# import travel.thailand

# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage

# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam

# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# from travel import *

# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# import inspect
# import random

# print(inspect.getfile(random))

# from bs4 import BeautifulSoup

# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())

import byme

byme.sign()
