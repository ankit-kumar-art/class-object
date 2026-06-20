#write a program to reverse a number
num=int(input("enterr a number :"))#12345
rev=0
while num>0:
    reminder=num % 10
    rev=rev*10+reminder
    num=num//10
print(rev)    


# s=input("enter a number")
# stack=[]
# for ch in s:
#     stack.append(ch)
# rev=""
# while stack:
#     rev=stack.pop()
#     rev+=1
# print(rev)   

# find the sum of digits of a number==============================
num=int(input("enter the number"))
sum=0
while num>0:
    digit=num%10
    sum=sum+digit
    num=num//10
print(sum)       