#============================find the maximum subarray======================
#==========================brute force============================
arr=list(map(int,input("enter array ").split()))
# maxi=float("-inf")
# for i in range(len(arr)):
#     total=0
#     for j in range(i,len(arr)):
#         total=total+arr[j]
#         maxi=max(total,maxi)
# print(maxi)     

#=================kadan algo============
# maxi=float("-inf")
# total=0
# for i in range(len(arr)):
#     total=total+arr[i]
#     maxi=max(total,maxi)
#     if total<0:
#         total=0
# print(maxi)     
best_ending=arr[0]
result=arr[0]
for i in range(1,len(arr)):
    v1=best_ending+arr[i]
    v2=arr[i]
    best_ending=max(v1,v2)
    result=max(result,best_ending)
print(result)    
    
    