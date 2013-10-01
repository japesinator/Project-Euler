sum_squares = 0

for i in range(1, 101):
    sum_squares += i ** 2

sum = 0

for i in range(1, 101):
    sum += i

square_sum = sum ** 2

print square_sum - sum_squares
