divisors=[]
n = int(input())
for i in range(1,n+1):
    if n%i==0:
        divisors.append(i)


def sumDigits(no): 
    return 0 if no == 0 else int(no%10) + sumDigits(int(no/10)) 

l=[sumDigits(x) for x in divisors]

if len(l)!=len(set(l)):
    maxl=max(l)
    ziplist=list(zip(divisors,l))
    endgame=[x for x,y in ziplist if y==maxl]
    print(min(endgame))
else:
    print(divisors[l.index(max(l))])
