
def min_coins(total,coins):

    T =[0 if c == 0 else float("inf") for c in range(total+1)]
    R = [0 for _ in range(total + 1)]

    for j in range(len(coins)):
        for i in range(1, total + 1):
            if i >= coins[j] and T[i] > 1 + T[i - coins[j]]:
                    T[i] = 1 + T[i - coins[j]]
                    R[i] = j
    
    start = total
    if R[start] == -1:
        print "No Solution Possible."
        return

    print "Coins:",
    while start != 0:
        coin = coins[R[start]]
        print "%d " % coin,
        start = start - coin

min_coins(11,[1,5,6,8])