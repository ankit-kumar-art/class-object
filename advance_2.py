'''
you are given an array of integers you have to find the number of opposite pairs
in the array.Two elements a[i] and a[j] form an opposite pair if a[i]==-a[j]and i<j
'''
# def countpair(arr):
#     n=len(arr)
#     count=0
#     for i in range(n):
#         for j in range(i+1,n):
#             if arr[i]==-arr[j]:
#                 count+=1
#     return count
     
# arr=list(map(int,input("enter array ").split()))
# print(countpair(arr))

#===========================unique pair=================================use set()
arr=list(map(int,input("enter array ").split()))
seen=set()
count=0
for num in arr:
    if -num in seen:
        count+=1
    seen.add(num)
print(count)
#==========================================================
 
        

            
