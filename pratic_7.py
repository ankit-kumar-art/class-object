# move zero to the end of array=================
# nums=[3,5,6,8,5,0,6,0,8,0]
# n=len(nums)
# zero=nums.count(0)
# for i in range(zero):
#     nums.remove(0)
#     nums.append(0)
# print(nums)   
#====================================== 
# temp=[]
# for i in range(n):
#     if nums[i]!=0:
#         temp.append(nums[i])
# n2=len(temp)
# for i in range(n2):
#     nums[i]=temp[i]
# for i in range(n2,n):
#     nums[i]=0
# print(nums)     

#-------------two pointer approach
def movezero(nums):
    j=0
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[j],nums[i]=nums[i],nums[j]
            j+=1
    return nums
nums=[1,2,3,0,7,0,4,3]
print(movezero(nums))           
            