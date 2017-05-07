#python2
# Author: Ashish Sardana
def gcdrec(a,b):
    if b==0:
        return a
    else:
       return gcdrec(b,a%b)

import sys
input = sys.stdin.read()
a, b = map(int, input.split())

#a=input()
#b=input()

print gcdrec(a,b)
