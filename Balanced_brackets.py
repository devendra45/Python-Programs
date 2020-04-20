
def isBalanced(s):
    l1=['[','(','{']
    l2=[']',')','}']
    #inp=[x for x in s]

    bal=[]
    for i in s:
        if i in l1:
            bal.append(i)
        else:
            bal.append(i)
            if len(bal)==1:
               break
            else:
                if l1.index(bal[-2])==l2.index(bal[-1]):
                    bal.pop()
                    bal.pop()
                else:
                    break
    if len(bal)==0:
        return "YES"
    else:
        return "NO"   

t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)
		print(result)