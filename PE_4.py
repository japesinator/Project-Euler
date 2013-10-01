
answer = 0

for i in range (100, 999):
    print i
    for j in range (first_num, 999):
        print i * j
        test_prod = i * j
        if i * j > answer:
            for char in range(0, len(str(test_prod))):
                if str(test_prod)[char] != str(test_prod)[len(str(test_prod)) - (char + 1)]:
                    break
                else:
                    if char > len(str(test_prod)) / 2:
                        answer = i * j

print answer
