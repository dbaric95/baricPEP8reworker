import re
with open('proba.py', "r") as original_file:
     import_content = ""
     content_string = ""
     countLine = 0
     counter = 0
     lista =[]
     for string in original_file.readlines():
         # print repr(string)
         if string.startswith(' '):
             lista.append(string)
             # print(lista)
             for i in lista[-1:1]:
                 print(i)
                 if i == ' ':
                     counter += 1
                 else:
                     break
         else:
             pass
             
         print(counter)
         #  matchMoreSpaces.replace("") aaaaaaaaaa aaaaaaaaaa aaaaaaaaaa\
         # aaaaaaaaaa
         matchMoreSpaces = re.sub("\s\s +", " ", string)
         # matchMoreSpaces=re.sub('\s+', ' ', string).strip()
         # print(matchMoreSpaces)