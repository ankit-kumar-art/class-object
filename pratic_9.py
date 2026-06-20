#3 sum=================


#======================================find maximum==========
#arr=list(map(int,input("enter the array ").split()))
#n=len(arr)
# max=arr[0]
# for num in arr:
#     if num>max:
#         max=num
# print(max)      

#=================================find second largest=====with sorting====
# arr=list(map(int,input("enter the array ").split()))
# n=len(arr)
# arr=sorted(set(arr))
# print(arr[-2])

#==========================without sorting===============
# def secondlargest(arr):
#     largest=float("-inf")
#     s_largest=float("-inf")
#     n=len(arr)
#     for i in range(n):    
#         largest=max(largest,arr[i])
#     for i in range(n):
#         if arr[i]>s_largest and arr[i]!=largest:
#             s_largest=arr[i]
#     return s_largest       
# arr=list(map(int,input().split()))
# print(secondlargest(arr))

#==============================================otimal===============
def secondlargest(arr):
    n=len(arr)
    largest=float("-inf")
    s_largest=float("-inf")
    for i in range(n):
        if arr[i]>largest :
            s_largest=largest
            largest=arr[i]
        elif arr[i] > s_largest and arr[i]!=largest:
            s_largest=arr[i] 
    return s_largest       
arr=list(map(int,input().split()))
print(secondlargest(arr)) 

 
                