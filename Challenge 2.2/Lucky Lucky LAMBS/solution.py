def mostStingy(total_lambs):
    #Bottom up calculation
    payout = [1]
    total_lambs -= 1
    while total_lambs >= 0:
        total_lambs -= payout[-1] * 2
        if total_lambs < 0: break
        payout.append(payout[-1] * 2)
    return(len(payout))
    
def mostGenerous(total_lambs):
    #Top Down Calculation
    payout = [1,1,2,3]
    total_lambs -= 7
    while total_lambs >= 0:
        total_lambs -= payout[-1] + payout[-2]
        if total_lambs < 0: break
        payout.append(payout[-1] + payout[-2])
    return(len(payout))
       
def answer(total_lambs):
    # your code here
    return(abs(mostStingy(total_lambs) - mostGenerous(total_lambs)))
