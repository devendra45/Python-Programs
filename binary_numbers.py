n = int(input())
rem=''
while(n):
    rem+=str(n%2)
    n//=2

bi=rem[::-1]
consec1=bi.split('0')
print(len(max(consec1)))