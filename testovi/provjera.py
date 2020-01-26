import re
with open('baricPEP.py', "r") as original_file:
    import_content = ""
    content_string = ""
    countLine = 0
    counter = 0
    lista = []
    for string in original_file.readlines():
        print(string)
        lista.append(string)
        if string.startswith(' '):
            #print("daaaaa")
            lista.append(string)
            for i in lista[-1]:
                print(i)
                if i == ' ':
                    counter+=1
                else:
                    break
        else:
            pass
        print(counter)
        #matchMoreSpaces.replace("")
        matchMoreSpaces = re.sub("\s\s +", " ", string)
        #matchMoreSpaces=re.sub('\s+', ' ', string).strip()
        #print(matchMoreSpaces)