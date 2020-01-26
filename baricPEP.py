# -*- coding: utf-8 -*-
##################################################
#
# Created by eDAB
# email: davor.baric@rt-rk.com
#
# Description:
#       PEP8 program
#
# Usage:
#      run cmd in folder -> python baricPEP.py -P pathToFolderWithTests
#
##################################################

# import modules
import os
import re
import argparse
import time
import sys


def start_program():
    print("-"*50)
    print("Created by: eDAB")
    print("Created by: Davor Baric")
    print("Email: Davor.Baric@rt-rk.com")
    print("Created: 15.01.2020.")
    print("      __    __   __      __    ")
    print("     |__|  |__  |__| __ |__|   ")
    print("     |     |__  |       |__|   ")
    print("-" * 50)

    toolbar_width = 20
    sys.stdout.write("Loading...[")
    for i in range(toolbar_width):
        time.sleep(0.1)
        sys.stdout.write("#")
    sys.stdout.write("] 100% Completed...\n")
    time.sleep(1)

    argPars = argparse.ArgumentParser(description="Enter the path to the tests")
    argPars.add_argument('-p', '--path', type=str, help="path to the folder")
    args = argPars.parse_args()
    path = args.path
    if path:
        print("Test folder path:", path)
    else:
        print("-" * 50)
        print("ERROR: Use -P path !!!")
        print("-"*50)

    return path


def max_len_line(string, count_line):
    content_string = ""
    counter2 = string.count("\t")

    if len(string) > 78 and len(string)< 160 and not("\t" * counter2 + "'''") in string:
        print("#" * 50)
        print("Line", count_line, "in ORIGINAL file is too long")
        print("#" * 50)
        string = re.sub(' +', ' ', string)
        # string = (re.sub('\s\s+', " ", string))
        flag = False
        counter = 0
        for i in string:
            counter += 1
            if counter <= 60 and flag is False:
                content_string += i
            # ADDITIONALLY: long comments in file(comment>78)
            elif i == ' ' and counter > 60 and flag is False and ("\t" * counter2 + "#") in string:
                flag = True
                content_string += '\\' + '\n' + '\t' * counter2 + "#"
            elif i == ' ' and counter > 60 and flag is False and ("\t" * counter2 + " #") in string:
                flag = True
                content_string += '\\' + '\n' + '\t' * counter2 + " #"
            # line without comment
            elif i == ' ' and counter > 60 and flag is False:
                flag = True
                content_string += '\\\n'
            else:
                content_string += i

    if len(string) > 78 and len(string)< 160 and ("\t" * counter2 + "'''") in string:
        print("#" * 50)
        print("Line", count_line, "in ORIGINAL file is too long")
        print("#" * 50)
        string = re.sub(' +', ' ', string)
        # string = (re.sub('\s\s+', " ", string))
        flag = False
        counter = 0
        for i in string:
            counter += 1
            if counter <= 60 and flag is False:
                content_string += i
            elif i == ' ' and counter > 60 and flag is False:
                flag = True
                content_string += '\\' + '\n' + '\t'
            else:
                content_string += i

    if len(string) >= 160 and not ("\t" * counter2 + "'''") in string:
        print("#" * 50)
        print("Line", count_line, "in ORIGINAL file is too long")
        print("#" * 50)
        string = re.sub(' +', ' ', string)
        # string = (re.sub('\s\s+', " ", string))
        flag = 0
        counter = 0
        for i in string:
            counter += 1
            if counter < 60 and flag == 0:
                content_string += i
            # line without comment
            elif i == ' ' and counter >= 60 and flag == 0:
                flag = 1
                content_string += '\\'+'\n'

            elif i != ' ' and counter > 60 or counter <= 130 and flag == 1:
                content_string += i

            elif i == ' ' and counter > 130 and flag == 1:
                flag = 2
                content_string += '\\'+'\n'

            elif flag == 2:
                content_string += i

    if len(string) >=160 and ("\t" * counter2 + "'''") in string:
        print("#" * 50)
        print("Line", count_line, "in ORIGINAL file is too long")
        print("#" * 50)
        string = re.sub(' +', ' ', string)
        # string = (re.sub('\s\s+', " ", string))
        flag = 0
        counter = 0
        for i in string:
            counter += 1
            if counter < 60 and flag == 0:
                content_string += i
            # line without comment
            elif i == ' ' and counter >= 60 and flag == 0:
                flag = 1
                content_string += '\n' + '\t' * counter2

            elif i != ' ' and counter > 60 or counter <= 130 and flag == 1:
                content_string += i

            elif i == ' ' and counter > 130 and flag == 1:
                flag = 2
                content_string += '\n' + '\t' * counter2

            elif flag == 2:
                content_string += i

    return content_string


def import_in_func(string):
    counter = string.count('\t')
    content_string = ""
    matchMoreSpaces = re.sub(' +', ' ', string)
    # matchMoreSpaces = (re.sub('\s\s+', " ", string))
    if "," in string:
        content_string += matchMoreSpaces.replace(",", '\n' + '\t' * counter + "import")
    else:
        content_string += matchMoreSpaces

    return content_string


def startswith_import(string):
    import_content = ""
    string = re.sub(' +', ' ', string)
    # string = (re.sub('\s\s+', " ", string))
    if "," in string:
        import_content += string.replace(",", "\nimport")
    else:
        import_content += string

    return import_content


def startswith_from(string):
    import_content = ""
    listaFrom = []
    string = re.sub(' +', ' ', string)
    #string = (re.sub('\s\s+', " ", string))
    listaFrom.append(string.split(" "))
    if "," in string:
        import_content += string.replace(",", "\nfrom " + listaFrom[0][1] + " " + listaFrom[0][2])
    else:
        import_content += string

    return import_content


def whitespaces(string):
    content_string = ""
    matchMoreSpaces = re.sub(' +', ' ', string)
    # matchMoreSpaces = (re.sub('\s\s+', " ", string))
    content_string += matchMoreSpaces.replace(' [', '[').replace(' :', ':'). \
        replace(': ', ':').replace(' (', '(').replace(' * ', '*'). \
        replace(' *', '*').replace('* ', '*').replace(')*(', ') * ('). \
        replace(', )', ',)').replace('( ', '(').replace('[ ', '['). \
        replace(' ]', ']')

    return content_string


def blank_spaces(string, listofString):
    content_string = ""
    operators = "= += -= * / + - < > != == <= >="

    # 4. SPACES(two blank spaces) between functions in modules and classes
    if any(op in string for op in operators) and listofString[-2] == "\n" \
            and listofString[-3] != "\n":
        matchMoreSpaces = re.sub(' +', ' ', string)
        # matchMoreSpaces = (re.sub('\s\s+', " ", string))
        content_string += "\n" + matchMoreSpaces.replace(" = ", "=")

    if any(op in string for op in operators) and listofString[-2] != "\n" \
            and listofString[-3] != "\n" and listofString[-2] != '\t\n':
        matchMoreSpaces = re.sub(' +', ' ', string)
        # matchMoreSpaces = (re.sub('\s\s+', " ", string))
        content_string += "\n\n" + matchMoreSpaces.replace(" = ", "=")

    if any(op in string for op in operators) and listofString[-2] == "\n" \
            and listofString[-3] == "\n":
        matchMoreSpaces = re.sub(' +', ' ', string)
        # matchMoreSpaces = (re.sub('\s\s+', " ", string))
        content_string += matchMoreSpaces.replace(" = ", "=")

    if any(op in string for op in operators) and listofString[-2] != "\n" and \
            listofString[-3] == "\n":
        matchMoreSpaces = re.sub(' +', ' ', string)
        # matchMoreSpaces = (re.sub('\s\s+', " ", string))
        content_string += matchMoreSpaces.replace(" = ", "=")

    # between func in classes
    if any(op in string for op in operators) and listofString[-2] == '\t\n' and \
            listofString[-3] != "\n":
        matchMoreSpaces = re.sub(' +', ' ', string)
        # matchMoreSpaces = (re.sub('\s\s+', " ", string))
        content_string += "\n" + matchMoreSpaces.replace(" = ", "=")

    return content_string


def write_content_in_copy_file(final_content_import, final_content, copy_file_name):
    new_file = open(copy_file_name, "w")
    new_file.write(final_content_import)
    new_file.write(final_content)
    return True


def string_startswith_space_no_tab(string, counterSpace):
    lista_string = []
    tmp_string = ''
    for i in string:
        if i != " ":
            break
        else:
            counterSpace += 1
            lista_string.append(i)
    if counterSpace >= 4:
        lista_string[0:counterSpace] = "\t" * (counterSpace/4)
        for i in lista_string:
            tmp_string += i
        string = tmp_string + string

    return string


def main(path):
    list_py_file = []
    no_py_file = []
    list_of_string = []

    for root, dirs, files in os.walk(path):
        for name in files:
            if name.endswith(".py"):
                print("-" * 50)
                print("Python file")
                print("OriginalName Test:", name)
                list_py_file.append(name)
                copy_file_name = "copyOf_" + "" + name
                print("TestCopy Name:", copy_file_name)
                print("-" * 50)
                print("-" * 50)

                with open(os.path.join(root, name), "r") as original_file:
                    import_content = ""
                    content_string = ""
                    count_line = 0
                    for string in original_file.readlines():
                        list_of_string.append(string)
                        #print repr(string)
                        count_line += 1
                        counterSpace = 0
                        # 1.IMPORT
                        if string.startswith("import"):
                            import_content += startswith_import(string)

                        # 1.1 IMPORT (from math import sys, os ..)
                        elif string.startswith("from"):
                            import_content += startswith_from(string)

                        else:
                            # String start with TAB or SPACE(4) ??????
                            # if start with space(4)
                            string = string_startswith_space_no_tab(string, counterSpace)

                            # 4. MAXIMUM LENGTH OF LINE - detect
                            if len(string) > 78:
                                content_string += max_len_line(string, count_line)

                            # 3. WHITESPACES
                            # whitespaces def and return
                            elif string.startswith("def") or "def" in string:
                                # 4. SPACES(two blank spaces) between functions in modules and classes
                                content_string += blank_spaces(string, list_of_string)

                            elif "return" in string:
                                string = re.sub(' +', ' ', string)
                                content_string += string.replace(" = ", "=").replace(" =", "=").replace("= ", "=")

                            else:
                                # import in function
                                if "\t" in string and "import" in string:
                                    content_string += import_in_func(string)
                                else:
                                    # whitespaces between variables, in array, call functions...
                                    content_string += whitespaces(string)

                    # 2. TAB TO SPACE
                    # ADDITIONALLY: comments in file, space between # and comment
                    final_content_import = import_content.replace('\t', '    ')
                    final_content = content_string.replace('\t', '    ').replace('#', '# ')

                    write_content_in_copy_file(final_content_import, final_content, copy_file_name)

            else:
                no_py_file.append(name)
                print("NOT Python file")

    return list_py_file, no_py_file


if __name__ == '__main__':
    path = start_program()
    files = main(path)
    print("All .py files in folder:\n\t", files[0])
    print("NO .py files in folder:\n\t", files[1])
