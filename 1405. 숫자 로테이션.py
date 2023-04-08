import sys
n = int(sys.stdin.readline())
num_lst = list(map(int,sys.stdin.readline().split()))

for i in range(n):
    print (*num_lst,end=' ')
    print()
    num_lst.append(num_lst.pop(0))
