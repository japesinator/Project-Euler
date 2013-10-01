
import math

a_list = []
b_list = []
c_list = []

for i in range(1, 20):
    for j in range(1, 20):
        if math.sqrt(i ** 2 + j ** 2) % 1 == 0:
            a_list.append(i)
            b_list.append(j)
            c_list.append(math.sqrt(i ** 2 + j ** 2))

for i in range(len(a_list)):
    if 1000 % (a_list[i] + b_list[i] + c_list[i]) == 0:
        scalar = 1000 / (a_list[i] + b_list[i] + c_list[i])
        print a_list[i], b_list[i], c_list[i]
        print scalar
        print a_list[i] * b_list[i] * c_list[i] * scalar **3
        break
