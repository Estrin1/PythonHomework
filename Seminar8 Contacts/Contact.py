

# f = open(file_path,'w')
# f.write("Hello World")
# f.close()
#
# r = open(file_path, 'r')
# for i in r:
#    print(r.readline())
# r.close()


# def writeinfile(file):
#
file_path = r'C:\Users\Евгений\Desktop\Тестирование\Python домашка\Seminar8 Contacts\Contact.txt'
# def fullfile(file):
#     with open(file_path, 'w', encoding= 'UTF -8' ) as f:
#         f.write("0\n")
#         f.write("Ivanov,Ilya,Ivanovich,89643764566")
#         f.write("Vil,Kalich,Gurevich,89765894534")
#         f.write("Aye,Yulia,Sergeevna,89653421836")

def readfile(file):
    with open(file, 'r') as f:
        for line in f:
            name, sname, Surname, Telephon = line.strip().split(',')
            contact = [name, sname, Surname, Telephon]
            print(contact)
            list1.append(contact)
    return list1

def rewritefile(file):
    with open(file, 'a') as f:
        f.write(input( "Введите новый контакт: фамилия,имя,отчество,номер телефона через запятую ")+"\n" )
    return file

def poisk(file):
    name = input("Введите имя или фамилию контакта: ").upper()
    with open(file,'r') as f:
        for line in f:
            if name in line: print(line)


def redact(file, list1):
    readfile(file)
    name = input("Введите имя или фамилию контакта который хотите редактировать: ")
    print(list1)
    for line in list1:
           if name in line:
               print(line)
               line.clear()
               line.append(input("Введите новые данные через запятую: "))
    print(list1)

    with open(file,'w') as f:
        for el in list1:
         f.write(el)



list1 = list()
print("Инструкция управления: r - прочитать файл, w - дописать контакт, p - найти контакт, a - перезаписать контакт")

command = input("Введите команду: ")
match command.split():
    case ["r"]:
        readfile(file_path)
    case ["w"]:
        rewritefile(file_path)
    case ["p"]:
        poisk(file_path)
    case ["a"]:
        redact(file_path, list1)

    case _:
        print(f"Не понял команду {command!r}")
