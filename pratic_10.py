'''
Pehle 2 items → ₹100 per item
Agle 3 items (3rd se 5th) → ₹50 per item
5 se zyada items → ₹30 per item
'''
try:
  input_str=input()
  n=int(input_str)
  if n<0:
    print("error")
  else:
    cost=0
    if n<=2:
        cost= n * 100
    elif n<=5:
        cost= (2 * 100) + (n-2)*50    
    else:
        cost= (2 *100)+(3 * 50)+(n-5)*30
    print(cost)
except:
    print("error")
            
        

