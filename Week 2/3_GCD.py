#python2
# Author: Ashish Sardana
import sys
input = sys.stdin.read()
a, b = map(int, input.split())

c = max(a,b)
d = min(a,b)
e = c%d

if e==0:
        gcd=d
else:
    for i in range(1,e+1):
        if d%i ==0 and e%i==0:
            gcd= i

       

print gcd

    
