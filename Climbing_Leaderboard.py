# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    rank=[]
    unique_sc=sorted(list(set(scores)),reverse=True)
    i=len(alice)-1
    j=0
    rank=0
    res=[]
    while(i>=0):
        if j>=len(unique_sc) or unique_sc[j]<=alice[i]:
            i-=1
            res.append(j+1)
        else:
            j+=1
    return reversed(res)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()



'''
Sample test case:
Input-->
7
100 100 50 40 40 20 10
4
5 25 50 120

output-->
6
4
2
1
'''