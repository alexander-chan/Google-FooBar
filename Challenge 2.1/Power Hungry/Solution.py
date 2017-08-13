from functools import reduce
def answer(xs):
    # your code here
    # Take in list, return max prod
    # Handle all abs(values) >= 1
    neg = [i for i in xs if i <= -1]
    pos = [i for i in xs if i >= 1]
    neg.sort(reverse = True)
    prod = 1
    #Edge cases
    if len(pos) == 0 and 0 in xs:
        return(str(0))
    if len(neg) == 1 and len(pos) == 0:
        return(str(neg[0]))
        
    #Main Solution
    if len(neg) > 1:
        if len(neg) % 2 == 0:
            prod = prod * reduce(lambda x, y: x*y, neg) 
        else:
            prod = prod * reduce(lambda x, y: x*y, neg[1:]) 
    if len(pos) >=  1:
        prod = prod * reduce(lambda x, y: x*y, pos)
        
    return(str(prod))
