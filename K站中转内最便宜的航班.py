from collections import defaultdict
from functools import lru_cache


# 方法一：自创朴素递归(深度优先？)（超时：通过测试用例27）
def findCheapestPrice1(n, flights, src, dst, k):
    # 建立记录节点所有出边的字典
    outMap = defaultdict(list)
    for s, d, p in flights:
        outMap[s].append([d,p])
    #print(outMap)
    ans = []
    def dfs(cur,count,spend):
        nonlocal ans
        if count-2>k:
            return
        if cur==dst:
            ans.append(spend)
            return
        for d, p in outMap[cur]:
            dfs(d,count+1,spend+p)
    dfs(src,1,0)
    return min(ans) if ans else -1

# 方法二：记忆化递归
def findCheapestPrice2(n, flights, src, dst, k):
    # 建立记录节点所有出边的字典
    outMap = defaultdict(list)
    for s, d, p in flights:
        outMap[s].append([d,p])
    @lru_cache(None)
    def dfs(cur,remain):
        if cur==dst:
            return 0
        if not remain:
            return float('inf')
        ans = float('inf')
        for d,p in outMap[cur]:
            ans = min(ans,dfs(d,remain-1)+p)
        return ans
    ans = dfs(src,k+1)
    return ans if ans!=float('inf') else -1
            

if __name__=='__main__':
    n = 5
    flights = [[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]]
    src = 2
    dst = 1
    k = 1
    print(findCheapestPrice2(n,flights,src,dst,k))
