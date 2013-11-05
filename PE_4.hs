palindromic x
    | reverse (show  x) == show x = True
    | otherwise                   = False

answer = maximum (filter palindromic [ x | y <- [100..999], z <- [100..999], let x = y * z])
