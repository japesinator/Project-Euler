import System.Environment
import Data.List

factors :: Int -> [Int]
factors n = nub ([ x | let y = fromIntegral n, x <- [2..floor (sqrt y)],  n `mod` x == 0 ] ++ [ z | let y = fromIntegral n, x <- [2..floor (sqrt y)], n `mod` x == 0, let z = n `div` x ])

abundant :: Int -> Bool
abundant n
    | sum (factors n) > n = True
    | otherwise           = False

abundant_nos = filter abundant [1..21612]

not_summable n
    | n `elem` [ x | a <- filter (<n) abundant_nos, b <- filter (<n) abundant_nos, let x = a + b ] = False
    | otherwise                                                                                    = True

answer = sum (filter not_summable [1..21612])

main = print answer
