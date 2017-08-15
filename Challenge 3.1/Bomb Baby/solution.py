
def answer(M, F):
    M, F = int(M), int(F)
    i = 0
    while M >= 1 and F >= 1 and not (M == 1 and F == 1):
        if M == F:
            return("impossible")
        elif M > F:
            iters = M // F
            M = M - F * (iters)
            i += iters
        else: 
            iters = F // M
            F = F - M * iters
            i += iters
    if M == 1 or F == 1:
        return(str(i - 1))
    else:
        return("impossible")
    

l1 = [6,6,9,9,11,11,10,10,13,13,11,11,12,12,9,9]
l2 = [5,1,5,4,7,4,7,3,5,8,3,8,5,7,2,7]
l3 = [5, 5, 7, 7, 8, 8, 7, 7 ]
l4 = [1, 4, 4, 3, 5, 3, 5, 2]

list(map(answer, l3 , l4))
