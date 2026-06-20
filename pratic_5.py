# write a program check whether two strings are anagrams
# s1=input("enter the first string :")
# s2=input("enter the second string :")

# if sorted(s1)==sorted(s2):
#     print("anagrams")
# else:
#     print("not anagrams")    
    
    
## 2 approach==================================
s1=input("enter the first string :")
s2=input("enter the second string :")
if len(s1)!=len(s2):
    print("not anagram")
freq={}
for ch in s1:
    if ch in freq:
        freq[ch]=freq.get(ch,0)+1
for ch in s2:
    if ch in freq:
        freq[ch]-=1
for value in freq.values():
    if value!=0:
        print("not Anagram") 
        break
    else:
        print("Anagram")              
            
            
    
    