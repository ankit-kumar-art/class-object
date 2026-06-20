''' At a coding club,
strings are considered beautiful if they do not contain any vowel.
The club president wants to check whether a given string follows this rule.
Note that vowels are 'a','e','i','o','u'and they can appear in both lowercase and uppercase forms.
input format :A single string 
output format print yes if the string is beautiful otherwise no

'''
s=input("enter the string")
vowels="aeiouAEIOU"
for ch in s:
    if ch in vowels:
        print("No")
        break
else:    
 print("yes")    

