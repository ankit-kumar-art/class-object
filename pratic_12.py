'''
input A = [1, 3, 5, 7]
      B = [8, 4, 5, 1]
'''

def mergee(A,B):
    i=0
    j=len(B)-1
    result=[]
    while i<len(A) and j>=0:
        if A[i]<=B[j]:
            result.append(A[i])
            i+=1
        else:
            result.append(B[j])
            j-=1
    while i<len(A):
        result.append(A[i])
        i+=1
    while j>=0:
        result.append(B[j])
        j-=1
    return result
n=int(input())
#==========3 4 5 7 4
A=list(map(int,input().strip().split()))
m=int(input())
B=list(map(int,input().strip().split()))  
res=mergee(A,B)
print(res)
  
