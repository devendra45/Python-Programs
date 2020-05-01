# this program sorts strings in following order:
# lowercase alphabets first --> uppercase aplhabets --> odd numbers--> even numbers
s=input()
uc=''
lc=''
odd=[]
even=[]
for i in s:
    if i.isupper()==True:
        uc+=i
    elif i.islower()==True:
        lc+=i
    elif i.isdigit() and int(i)%2==0:
        even.append(int(i))
    else:
        odd.append(int(i))
lc=''.join(sorted(lc))
uc=''.join(sorted(uc))
od=''.join(map(str,sorted(odd)))
ev=''.join(map(str,sorted(even)))
print(lc+uc+od+ev) 
