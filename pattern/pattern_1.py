'''
*
**
***
****
*****
'''

# n=int(input("enter the number :"))
# for i in range(1,n):
#     for j in range(1,i+1):
#         print("*",end="") 
#     print()    
'''
    *
   **
  ***
 ****
*****      
'''
for i in range(1,6):
    for j in range(5-i):
        print(" ",end="")
    for k in range(i):
        print("*",end="")
    print()    
            
