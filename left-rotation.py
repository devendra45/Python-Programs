nd = input().split()

n = int(nd[0])

d = int(nd[1])

a = list(map(int, input().rstrip().split()))

a=a[d:]+a[0:d]
print(*a)
