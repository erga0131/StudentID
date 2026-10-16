import numpy as np

id_input = input("学籍番号の上7桁を入力して下さい: ")

id = np.zeros((7,1))
weight = np.zeros((1, 7))

for i in range(7):
    weight[:,i] = int((i + 2))
for i in range(7):
    id[i] = int(id_input[i:i+1])

sum = np.dot(weight, id)
amari = sum % 11

if amari == 1:
    num = 0
else:
    num = int(11 - amari[0,0])

print("YOUR STUDENT ID IS: "+id_input+str(num))
