#wap to check whether a string is palindrome or not
# def checkpalidrom(s):
#     n=len(s)
#     low=0
#     high=n-1
#     while low<high:
#       if s[low]!=s[high]:
#          return False
#       low+=1
#       high-=1
#     return True  
     
#     return True 
# s=input("enter the string :")
# result=checkpalidrom(s)
# print(result)  
s=input("enter the string :")
rev=s[::-1]
if s==rev:
    print(True)
else:
    print(False)    
        