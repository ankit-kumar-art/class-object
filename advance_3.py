'''
rohit is given two strings s and t.
he can perform the following operations any number of times.
delete the first character of s and append it to the end of s check if he can
make the string s equal to string t
'''
s=input("enter the first string :")
t=input("enter the second string ")
n=len(s)
# if len(s)!=len(t):
#     print("no")
# elif t in (s+s):
#     print("yes")
# else:
#     print("nO")  
for i in range(n):
    s=s[1:]+s[0]
    if s==t:
        print("yes")
        break
    else:
     print("NO")    

