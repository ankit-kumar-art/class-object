#=====================two sum================
def two_sum(coins,target):#[4,5,6,4,3]  target=8\
    hash_map={}
    for i in range(len(coins)):
        need=target-coins[i]
        if need in hash_map:
            return [hash_map[need],i]
        hash_map[coins[i]]=i
    return [-1,-1]    
n=int(input())
coins=list(map(int,input().split()))
target=int(input())
result=two_sum(coins,target)
print(result[0],result[1])        
        
        
        