#python2
# Author: Ashish Sardana
import sys

m = int(sys.stdin.read())
n = 0

x = m/10
xi= m%10
y = xi/5
yi= xi%5

n = x+y+yi

print n
