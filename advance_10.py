'''
Given a string s, reverse the order of words in the string.A word is defined as a maximal substring consisting of non-space charcters only.

'''
n=int(input())
for _ in range(n):
    words=input()
    if len(words)>10:
        print(words[0]+str(len(words)-2)+words[-1])
    else:
        print(words)    