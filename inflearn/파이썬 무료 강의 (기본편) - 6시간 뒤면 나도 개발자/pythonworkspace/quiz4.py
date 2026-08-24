from random import *

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
shuffle(lst)

winner = sample(lst, 4)

print("--- 당첨자 발표 ---")
print("치킨 당첨자 : " + str(winner[0]))
print("커피 당첨자 : " + str(winner[1:]))
print("--- 축하합니다 ---")
