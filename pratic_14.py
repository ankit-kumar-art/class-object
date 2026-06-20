str = input()
if str=="":
    print("error")
else:
    ans=""
    for i,ch in enumerate(str):
          if i%2==0:
              if ch=="Z":
                  ans=ans+"B"
              elif ch=="z":
                  ans=ans+"b"
              elif ch=="8":
                  ans=ans+"0"   
              else:    
                  ans += chr(ord(ch) + 2)
          else:
              if ch == 'A':
                 ans += 'Z'
              elif ch == 'a':
                ans += 'z'
              elif ch == '0':
                 ans += '9'
              else:
                 ans+=chr(ord(ch)-1)
    print(ans)          
                  

























# if " " in s:
#     print("Error")
# else:
#     ans = ""

#     for i, ch in enumerate(s):

#         if i % 2 == 0:  # Even Index : +2

#             if ch == 'Z':
#                 ans += 'B'
#             elif ch == 'z':
#                 ans += 'b'
#             elif ch == '8':
#                 ans += '0'
#             elif ch == '9':
#                 ans += '1'
#             else:
#                 ans += chr(ord(ch) + 2)

#         else:  # Odd Index : -1

#             if ch == 'A':
#                 ans += 'Z'
#             elif ch == 'a':
#                 ans += 'z'
#             elif ch == '0':
#                 ans += '9'
#             else:
#                 ans += chr(ord(ch) - 1)

#     print(ans)