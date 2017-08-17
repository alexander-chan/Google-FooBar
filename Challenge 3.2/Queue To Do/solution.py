def subXOR(n):
    res = [n, 1, n+1, 0]
    return(res[n%4])

def XOR_range(a,b):
    return(subXOR(b) ^ subXOR(a-1))

def answer(start, length):
    sol = XOR_range(start, length-1 +start)
    #sol = reduce(xor, [i + start for i in range(length)])
    for i in range(2, length + 1):
            #sol = sol ^ reduce(xor, [j + start for j in range(length*(i-1),(length - 1)*i + 1)])
            sol = sol ^ XOR_range(length*(i-1) + start, (length - 1) * i + start)
    return(sol

# Solution inspired by mathematical numerical analysis from this resource:
# https://stackoverflow.com/questions/10670379/find-xor-of-all-numbers-in-a-given-range
