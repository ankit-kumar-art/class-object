#  first occurrence of target in an array

''''
arr=[4, 5, 4, 5, 3]
target=2
'''
arr=list(map(int,input().strip("[]").split(",")))
target=int(input())
def occurance(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
         return i
    return -1

res=occurance(arr)
print(res)
