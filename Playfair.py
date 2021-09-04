from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import Combobox
from tkinter import messagebox

def clicked():
    txt_original = txt.get("1.0", 'end-1c').lower()
    txt2.delete(1.0, END)
    key=txt3.get("1.0", 'end-1c').lower()
    eng_low_alphabet = 'abcdefghiklmnopqrstuvwxyz'
    rus_low_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщыьэюя'
    alphabet = ''
    temp_flag = 0
    txt_original = txt_original.replace(" ", "")
    txt_original = txt_original.replace("j", "i")
    key = key.replace("j", "i")

    txt_original = txt_original.replace("ъ", "ь")
    key = key.replace("ъ", "ь")


    for i in txt_original:
        if eng_low_alphabet.find(i, 0) != -1:
            alphabet = eng_low_alphabet
            break
        elif rus_low_alphabet.find(i, 0) != -1:
            alphabet = rus_low_alphabet
            break
    if alphabet == '':
        temp_flag = 1
        messagebox.showinfo('Ошибка!', f'Не удалось определить алфавит!')

    for i in key:
        if alphabet.find(i, 0) == -1:
            temp_flag = 1
            messagebox.showinfo('Ошибка!', f'Не совпадают алфавиты у шифруемого сообщения и ключа 1!')
            break


    if temp_flag==0:
        length = 1
        temporary_string = ''
        temporary_string = temporary_string + txt_original[0]

        while length < len(txt_original):
            if len(temporary_string) % 2 == 1:
                if txt_original[length] == temporary_string[len(temporary_string) - 1]:
                    if txt_original[length]=='x':
                        temporary_string = temporary_string + 'y' + txt_original[length]
                    else:
                        temporary_string = temporary_string + 'x' + txt_original[length]
                else:
                    temporary_string = temporary_string + txt_original[length]
            else:
                temporary_string = temporary_string + txt_original[length]

            length += 1
        if len(temporary_string) % 2 == 1:
            if temporary_string[len(temporary_string)-1]=='x':
                temporary_string = temporary_string + 'y'
            else:
                temporary_string = temporary_string + 'x'


        txt_original=temporary_string
        print(f'биграммная строка: {txt_original}')

        #делаем матрицу в которой будем сравнивать числа
        new=''
        for i in range(len(key)):
            if new.find(key[i],0)==-1:
                new=new+key[i]

        for i in range(len(alphabet)):
            if new.find(alphabet[i], 0) == -1:
                new = new+alphabet[i]

        print(new)

        if len(alphabet)==25:
            A=['']*5
            for i in range(len(A)):
                A[i]=['']*5

        elif len(alphabet)==32:
            A=['']*4
            for i in range(len(A)):
                A[i]=['']*8
        index=0
        for rows in range(len(A)):
            for cols in range(len(A[rows])):
                A[rows][cols]=new[index]
                index+=1

        for i in range(len(A)):
            for j in range(0, len(A[i])):
                print(A[i][j], end=' ')
            print()



        #шифрование
        if combo2.get() == "Зашифровать":
            for i in range(0,len(txt_original),2):
                coord1=['','']
                coord2=['','']
                for rows in range(len(A)):
                    for cols in range(len(A[rows])):
                        if txt_original[i]==A[rows][cols]:
                            coord1[0]=rows
                            coord1[1]=cols

                        elif txt_original[i+1]==A[rows][cols]:
                            coord2[0] = rows
                            coord2[1] = cols

                print(coord1)
                print(coord2)

                if coord1[0]==coord2[0]:
                    if coord1[1]==len(A)-1:
                        txt2.insert(INSERT, A[coord1[0]][0])
                        print(A[coord1[0]][0])
                    else:
                        txt2.insert(INSERT, A[coord1[0]][coord1[1] + 1])
                        print(A[coord1[0]][coord1[1] + 1])


                    if coord2[1] == len(A) - 1:
                        txt2.insert(INSERT, A[coord2[0]][0])
                        print(A[coord2[0]][0])
                    else:
                        txt2.insert(INSERT, A[coord2[0]][coord2[1] + 1])
                        print(A[coord2[0]][coord2[1] + 1])



                elif coord1[1]==coord2[1]:
                    if coord1[0]==len(A)-1:
                        txt2.insert(INSERT, A[0][coord1[1]])
                        print(A[0][coord1[1]])
                    else:
                        txt2.insert(INSERT, A[coord1[0]+1][coord1[1]])
                        print(A[coord1[0]+1][coord1[1]])


                    if coord2[0] == len(A) - 1:
                        txt2.insert(INSERT, A[0][coord2[1]])
                        print(A[0][coord2[1]])
                    else:
                        txt2.insert(INSERT, A[coord2[0]+1][coord2[1]])
                        print(A[coord2[0]+1][coord2[1]])


                elif ((coord1[0]!=coord2[0]) & (coord1[1]!=coord2[1])):
                    print('разный')
                    txt2.insert(INSERT, A[coord1[0]][coord2[1]])
                    txt2.insert(INSERT, A[coord2[0]][coord1[1]])
                    print(A[coord1[0]][coord2[1]])
                    print(A[coord2[0]][coord1[1]])


        elif combo2.get() == "Расшифровать":
            for i in range(0,len(txt_original),2):
                coord1=['','']
                coord2=['','']
                for rows in range(len(A)):
                    for cols in range(len(A[rows])):
                        if txt_original[i]==A[rows][cols]:
                            coord1[0]=rows
                            coord1[1]=cols

                        elif txt_original[i+1]==A[rows][cols]:
                            coord2[0] = rows
                            coord2[1] = cols

                print(coord1)
                print(coord2)

                if coord1[0]==coord2[0]:
                    if coord1[1]==0:
                        txt2.insert(INSERT, A[coord1[0]][len(A)-1])
                        print(A[coord1[0]][len(A)-1])
                    else:
                        txt2.insert(INSERT, A[coord1[0]][coord1[1] - 1])
                        print(A[coord1[0]][coord1[1] - 1])


                    if coord2[1] == 0:
                        txt2.insert(INSERT, A[coord2[0]][len(A)-1])
                        print(A[coord2[0]][len(A)-1])
                    else:
                        txt2.insert(INSERT, A[coord2[0]][coord2[1] - 1])
                        print(A[coord2[0]][coord2[1] - 1])



                elif coord1[1]==coord2[1]:
                    if coord1[0]==0:
                        txt2.insert(INSERT, A[len(A)-1][coord1[1]])
                        print(A[len(A)-1][coord1[1]])
                    else:
                        txt2.insert(INSERT, A[coord1[0]-1][coord1[1]])
                        print(A[coord1[0]-1][coord1[1]])


                    if coord2[0] == 0:
                        txt2.insert(INSERT, A[len(A)-1][coord2[1]])
                        print(A[len(A)-1][coord2[1]])
                    else:
                        txt2.insert(INSERT, A[coord2[0]-1][coord2[1]])
                        print(A[coord2[0]-1][coord2[1]])


                elif ((coord1[0]!=coord2[0]) & (coord1[1]!=coord2[1])):
                    print('разный')
                    txt2.insert(INSERT, A[coord1[0]][coord2[1]])
                    txt2.insert(INSERT, A[coord2[0]][coord1[1]])
                    print(A[coord1[0]][coord2[1]])
                    print(A[coord2[0]][coord1[1]])

def swap():
    temp1=txt2.get("1.0", 'end-1c')
    txt.delete(1.0, END)
    txt.insert(INSERT, temp1)
    txt2.delete(1.0, END)





window = Tk()
window.title("Шифр Плейфера")
window.geometry('500x200')

lbl = Label(window, text="Исходный текст")
lbl.grid(column=0, row=0)


lbl = Label(window, text="ключ")
lbl.grid(column=0, row=3)

txt3 = scrolledtext.ScrolledText(window, width=40, height=1)
txt3.grid(column=2, row=3)


combo2 = Combobox(window)
combo2['values'] = ("Зашифровать", "Расшифровать")
combo2.current(0)
combo2.grid(column=0, row=4)



btn = Button(window, text="Получить ответ", command=clicked)
btn.grid(column=0, row=5)
lbl = Label(window)

btn = Button(window, text="преместить", command=swap)
btn.grid(column=2, row=4)
lbl = Label(window)


txt = scrolledtext.ScrolledText(window, width=40, height=1)
txt.grid(column=2, row=0)

txt2 = scrolledtext.ScrolledText(window, width=40, height=1)
txt2.grid(column=2, row=5)


window.mainloop()

