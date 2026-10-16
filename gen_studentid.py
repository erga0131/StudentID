import random
import numpy as np

num = input("生成件数: ")

student_id = ""

weight = np.zeros(7)

for j in range(7):
    weight[j] = int((j + 2))

for i in range(int(num)):
    d1 = random.randint(1, 7)
    # 2, 3桁目: 入学年度 (20〜29)
    d2 = 2
    d3 = random.randint(20, 29) % 10
    # 4〜7桁目: ランダムな4桁
    d4 = random.randint(0, 9)
    d5 = random.randint(0, 9)
    d6 = random.randint(0, 9)
    d7 = random.randint(0, 9)

    digits = [d1, d2, d3, d4, d5, d6, d7]

    summation = np.dot(weight, digits).astype(int)
    amari = (summation % 11)
    if amari == 1:
        d8 = 0
    elif amari == 0:
        d8 = 1
    else:
        d8 = int(11 - amari)

    student_id = "".join(map(str, digits)) + str(d8)

    print("["+str(i)+" / "+num+"]")

    with open("studentid.txt", "a") as f:
        f.write(student_id + "\n")
