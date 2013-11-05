import Data.Numbers.Primes

answer = last [ x | x <- primeFactors 600851475143 ]
