# Distribute candies to the people
'''
ques-->We distribute some number of candies, to a row of n = num_people people in the following way:

We then give 1 candy to the first person, 2 candies to the second person, and so on until we give n candies to the last person.

Then, we go back to the start of the row, giving n + 1 candies to the first person, n + 2 candies to the second person, and so on until we give 2 * n candies to the last person.

This process repeats (with us giving one more candy each time, and moving to the start of the row after we reach the end) until we run out of candies.  The last person will receive all of our remaining candies (not necessarily one more than the previous gift).

Return an array (of length num_people and sum candies) that represents the final distribution of candies.
---------------------------------------------------------------------------------------------------------------------------------
Example:-

Input: candies = 10, num_people = 3
Output: [5,2,3]
Explanation: 
On the first turn, ans[0] += 1, and the array is [1,0,0].
On the second turn, ans[1] += 2, and the array is [1,2,0].
On the third turn, ans[2] += 3, and the array is [1,2,3].
On the fourth turn, ans[0] += 4, and the final array is [5,2,3].


'''
# Solution

def distributeCandies(self, candies, num_people):
       
        n=num_people
        nums=[0]*num_people
        it=0
        while(candies>0): #30
            for i in range(1,n+1):# 1 2 3
                if candies>=it*n+i and candies>0: # true 
                    nums[i-1]+=it*n+i   # 1->1 
            
                else:
                    if candies>0:
                        nums[i-1]+=candies
                candies-=(it*n+i)  # 29
            it+=1
        return nums