'''
Given an array of integers find the element that appears more than n/2 times in the array.
it is guaranteed that such an element exists.
'''
n=int(input("enter"))
arr=list(map(int,input().split()))
freq={}
for num in arr:
    freq[num]=freq.get(num,0)+1
for key in freq:
    if freq[key] >n//2:
        print(key)
        break
    
         