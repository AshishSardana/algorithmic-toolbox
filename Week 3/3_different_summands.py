# Uses python3
# Author: Ashish Sardana
import sys

def optimal_summands(n):
    summands = []
    #write your code here
    if n==1:
        summands[0] = 1
    elif n ==2:
        summands[0] = 2
    else:
        summands[0] = 1
        
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
