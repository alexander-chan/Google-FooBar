def mostStingy(total_lambs):
    #Bottom up calculation
    payout = [1]
    total_lambs -= 1
    while total_lambs >= payout[-1] * 2:
        total_lambs -= payout[-1] * 2
        payout.append(payout[-1] * 2)
    #Filler henchmen for rule #4
    while total_lambs >= payout[-1] + payout[-2]:
        total_lambs -= payout[-1] + payout[-2]
        payout.append(payout[-1] + payout[-2])
    return(len(payout))
    
def mostGenerous(total_lambs):
    #Top Down Calculation
    payout = [1,1,2,3]
    total_lambs -= 7 #initial payout
    while total_lambs >= payout[-1] + payout[-2]:
        total_lambs -= payout[-1] + payout[-2]
        payout.append(payout[-1] + payout[-2])
    return(len(payout))
        
def answer(total_lambs):
    # your code here
    if total_lambs < 10 or total_lambs > 1e9:
        return(0)
    return(abs(mostStingy(total_lambs) - mostGenerous(total_lambs)))

