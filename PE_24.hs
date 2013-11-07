import Data.List
strToInt n = read n :: Int
answer = sort (map strToInt (permutations "0123456789")) !! 999999
