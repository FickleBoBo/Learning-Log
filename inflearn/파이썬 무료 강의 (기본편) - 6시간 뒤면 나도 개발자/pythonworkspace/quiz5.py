from random import *

cnt = 0
for i in range(1, 51):
    x = randint(5, 50)
    if 5 <= x <= 15:
        print(f"[O] {i}번째 손님 (소요시간 : {x}분)")
        cnt += 1
    else:
        print(f"[ ] {i}번째 손님 (소요시간 : {x}분)")

print(f"총 탑승 승객 : {cnt} 분")
