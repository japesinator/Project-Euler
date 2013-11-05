fib n
    | n == 0 || n == 1 = 1
    | otherwise = fib(n - 1) + fib(n - 2)
fibnos = map fib [0..]

answer = sum [x | x <- takeWhile (<=4000000) fibnos, even x]
