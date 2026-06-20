# wap to find the index of the first Non-Repeating Character in a string.
s=input("enter the string :")
hash_map={}
for ch in s:
    if ch in hash_map:
        hash_map[ch]+=1
    else:
        hash_map[ch]=1
for i in range(len(s)):    
  if hash_map[s[i]]==1:
    print(s[i])
    break      
            
    