from functools import reduce
def answer(xs):
    # your code here
    # Take in list, return max prod
    # Handle all abs(values) >= 1
    neg = [i for i in xs if i <= -1]
    pos = [i for i in xs if i >= 1]
    neg.sort(reverse = True)
    prod = 1
    if len(neg) > 1:
        if len(neg) % 2 == 0:
            prod = prod * reduce(lambda x, y: x*y, neg) 
        else:
            prod = prod * reduce(lambda x, y: x*y, neg[1:]) 
    if len(pos) >=  1:
        prod = prod * reduce(lambda x, y: x*y, pos)
        
    ### If no  > 1 solutions available, 
    if len(neg) <= 1 and len(pos) < 1:
        negDEC = [i for i in xs if i < 0 and i > -1]
        posDEC = [i for i in xs if i > 0 and i < 1]
        if len(negDEC) > 1:
            negDEC.sorted()
            negSol = negDEC[0] * negDEC[1]
        if len(posDEC) > 0:
            posDEC.sort(reverse = True)
            posSol = posDEC[0]
        if len(negDEC) > 1 and len(posDEC) > 0:
            prod = negSol if negSol > posSol else posSol
        elif len(negDEC) > 1:
            prod = negSol
        elif len(posDEC) > 0:
            prod = posSol
    return(str(prod))
