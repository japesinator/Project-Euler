answer = 1
divisible = False

while divisible == False:
    answer += 1
    divisible = True
    for i in range(1, 21):
        if (2520 * 19 * 17 * answer) % i != 0:
            divisible = False

print 2520 * 19 * 17 * answer

