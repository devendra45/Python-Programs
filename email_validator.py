import re
N = int(input())
    l=[]
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
        
        if len(firstName)<=20 and len(emailID)<=50:
            if re.search(r'[a-z]+',firstName) and re.search(r'^[a-z]+\.*[a-z]*@gmail(\.)com',emailID): #email contains only @gmail.com
                l.append(firstName)
            else:
                continue
    for i in sorted(l):  
        print(i)