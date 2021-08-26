
"""
2021.8.27
分析：
由于每艘救生艇最多坐两人，考虑让每艘救生艇在不超过两人的情况下达到最大承重。

预处理：
可将所有人按体重升序排序，利用双指针分别指向当前最重和最轻的两人。

实现逻辑：
若当前双指针所指两人重量和在limit限制内，即能同时运走，则ans+1，双指针相向移动
否则右指针移动，即运走更重的那个，ans+1
"""
# 贪心选择+双指针
def numRescueBoats(people, limit):
    n, ans = len(people), 0
    people.sort()
    left, right = 0, n-1

    while left<=right:
        ans += 1
        if people[right]+people[left]<=limit:
            left, right = left+1, right-1
        else:
            right -= 1
    
    return ans 

if __name__=='__main__':
    people = [1,2,4,4,3,5]
    limit = 6
    print(numRescueBoats(people,limit))
