def countApplesAndOranges(s, t, a, b, apples, oranges):
    app=0
    org=0
    applist=[i+a for i in apples]
    orglist=[i+b for i in oranges]
    for i in applist:
        if i>=s and i<=t:
            app+=1
    for i in orglist:
        if i>=s and i<=t:
            org+=1
    print(app)
    print(org)
if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
