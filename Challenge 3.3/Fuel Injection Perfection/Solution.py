def findIters(n):
    if n in memo:
        #If present in Memo, no need to calculate again
        return(memo[n])
    if n % 2 == 0:
        # For even numbers, divide by 2.
        sol = findIters(n / 2)
        # Add 1 step to divide.
        memo[n] = sol + 1
    else:     
        # For odd numbers, find closest odd number. 
        upper = (n + 1) / 2
        lower = (n - 1) / 2
        # Add two steps. One step to increment/decrement.
        # One step for division.
        if upper % 2 == 0:
            memo[n] = findIters(upper) + 2
        elif lower % 2 == 0:
            memo[n] = findIters(lower) + 2
        else:
            print("should not go here")
    return(memo[n])

def answer(n):
    # your code here
    n = int(n)
    if n == 1:
        return(0)
    elif n == 2:
        return(1)
    elif n > int('9' * 309):
        return(0)
        
    # Memoization Dictionary
    global memo 
    memo = {1: 0, 2: 1, 3: 2}

    return(findIters(n))
