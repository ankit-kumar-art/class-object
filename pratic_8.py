# write a program to remove duplicate value of sorted array
##======================brute force=============
# def removeDuplicates(nums):
#     n=len(nums)
#     freq_map={}
#     for i in range(n):
#         freq_map[nums[i]]=0
#     j=0
#     for k in freq_map:
#         nums[j]=k
#         j+=1
#     return j        
def removeDuplicates(nums):
        n=len(nums)
        if n==1:
            return 1
        i=0
        j=i+1
        while j<n:
            if nums[i]!=nums[j]:
                i+=1
                nums[i],nums[j]=nums[j],nums[i]
            j+=1    
        return i+1    
            
nums=[2,3,4,5,5,5,4,6]    
print(removeDuplicates(nums))