# Right rotate from one place
nnums=[3,4,6,3,7,5,7,4,3,4]
#k=9
#===============list slicing=================
# print(nums)
#=len(nums)
# nums[:]=nums[-1:]+nums[0:n-1]
# print(nums)

#-======================loop
# temp=nums[-1]
# for i in range(n-2,-1,-1):
#     nums[i+1]=nums[i]
# nums[0]=temp    
# print(nums)
   
##========================================    Right rotate an array by k places
# rotation=k%n
# for _ in range(rotation):
#     e=nums.pop()
#     nums.insert(0,e)
# print(nums)    

#==================================slicing=============
# k=n%k
# nums[:]=nums[n-k:n]+nums[0:n-k]
# print(nums)

#====================================otimal==========================
nums=[3,4,3,3,2,22,7,8,6,54]
n=len(nums)
k=5
k=k%n

def reverse(nums,left,right):
    while left<right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1

reverse(nums,n-k,n-1)
reverse(nums,0,n-k-1)
reverse(nums,0,n-1)   
print(nums)     
    
    
    



    
    
        

