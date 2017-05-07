#python2
# Author: Ashish Sardana
import sys
input = sys.stdin.read()
n = int(input)
sum =0

if n==0:
    sum=0
elif n==1:
    sum =1
else:
    for i in range(2,n+1):
        sum = (sum + i)%10

print sum
    



