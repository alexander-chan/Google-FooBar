import math
def answer(n):
    # your code here
    ##Create Prime String
    primeString = ""
    primeString += str(2)
    num = 1
    while len(primeString) <= 10005:
        num += 2
        if all(num % i != 0  for i in range(2,int(math.sqrt(num)) + 1)):
            primeString += str(num)
    #Return solution
    return(primeString[n:n+5])
