fname = input("Введите имя файла: ")
file_opened = False
while file_opened == False:
    try:
        inf = open(fname, "r")
        file_opened = True
    except FileNotFoundError:
        print("Файл '%s' не найден. Попробуйте еще.")
        fname = input("Введите имя файла: ")
#inf = open("C:/Users/User/Downloads/words.txt", "r")
flag = True
for row in inf:
    if "a" in row:
        count = row.count("a")
        if count == 1:
            flag = True
        else: flag = False
    if flag == True and "e" in row:
        count = row.count("e")
        if count == 1:
            flag = True
        else: flag = False
    if flag == True and "i" in row:
        count = row.count("i")
        if count == 1:
            flag = True
        else: flag = False
    if flag == True and "o" in row:
        count = row.count("o")
        if count == 1:
            flag = True
        else: flag = False
    if flag == True and "u" in row:
        count = row.count("u")
        if count == 1:
            flag = True
        else: flag = False
    if flag == True and "y" in row:
        count = row.count("y")
        if count == 1:
            flag = True
        else: flag = False
    if flag == True:
        index = row.find("a")
        index2 = row.find("e")
        index3 = row.find("i")
        index4 = row.find("o")
        index5 = row.find("u")
        index6 = row.find("y")
        if (index != -1) and (index < index2 < index3 < index4 < index5 < index6):
            print (row)
