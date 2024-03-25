##ПОМЕНЯТЬ НА НЕОБХОДИМУЮ ДИРЕКТОРИЮ

##import os
##os.chdir("c:\\Users\\Лия\\Documents\\it\\pythonuni\\sr_var11\\1")
## считывание инпута

with open("input1.txt", "r") as file:
    lines = file.readlines()

##разделение слов, удаление перехода на сл строку
sentence=lines[0].split(": ")
sentence[-1]=sentence[-1].rstrip("\n")

##число ошибки
num=int(lines[1])

##создание строки для вывода
solution=""


for word in sentence:
    l=len(word)

    ##проверка условия
    if l>num and l%num!=0:

        ##вставка с заглавной буквы, разделение запятой и пробелом
        solution+=word.title()+", "

##лишние запятая и пробел у посл элемента
solution=solution[:-2]

##аутпут
with open("output.txt", "w") as file:
    file.write(solution)