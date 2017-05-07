# Uses python3
# Author: Ashish Sardana
import sys
import random

def partition3(a, s, e):
    key = a[e]
    l = int(e - s + 1)
    i = -1
    k = l
    B = [0 for x in range(l)] #new list - same size as original list (a)
    for j in range(s, e):
        if a[j] < key:
            i = i + 1
            B[i] = a[j]

        elif a[j] > key:
            k = k - 1
            B[k] = a[j]
           
    for j in range(i + 1, k):
        B[j] = key


    for j in range(s, e + 1):
        a[j] = B[j - s]
    return (2 * s + i + k) // 2

def partition2(a, s, e):
    key = a[e]
    j = s;
    for i in range(s,e):
        if a[i] <= key:
            a[i], a[j] = a[j], a[i]
            j += 1
    a[e], a[j] = a[j], a[e]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k =random.randint(l, r)
    a[r], a[k] = a[k], a[r]
    m = partition3(a, l, r)
    #m = partition2(a, l, r)
    randomized_quick_sort(a, l, m - 1);
    randomized_quick_sort(a, m + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a =list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
