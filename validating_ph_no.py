t=int(input())
import re
for i in range(t):
    ph=input()
    s=''
    s=''.join((re.findall(r'\d+',ph)))
    valid=['7','8','9']
    if len(s)>0:
        if s[0] in valid and len(s)==10 and len(ph)==10:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
