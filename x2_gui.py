#Program for solving complete square equations , include graphical interface
#August 2020

#Программа для решения квадратных уравнений , графический интерфейс присутсвует
#Август 2020

from tkinter import *
from tkinter import messagebox

a = 0
b = 0
c = 0
d = 0
x1 = 0
x2 = 0


#Создание окна  
windowdone = Tk()
windowdone.title("The solution of quadratic equations")
windowdone.geometry('650x400')



def click():
    a = int(entryA.get())
    b = int(entryB.get())
    c = int(entryC.get())
    d = (b*b)-(4*a*c)
    labelD.configure(text = round(d,3))
    if d == 0:
        x1 = (-b+d)/(2*a)
        round(x1 , 3)
        labelx1.configure(text = x1)
    if d > 0:
        labelD.configure(text = round(d , 3))
        d = pow(d,0.5)
        labelDiz.configure(text = round(d , 3))
        x1 = (-b+d)/(2*a)
        x2 = (-b-d)/(2*a)
        x1 = round(x1 , 3)
        x2 = round(x2 , 3)
        labelx1.configure(text = x1)
        labelx2.configure(text = x2)

    if d < 0:
        labelD.configure(text = round(d , 3))
        messagebox.showinfo('Нет решения ', 'Нет решения так как дискриминант меньше 0 ')

        
    
#Создание пунктов для ввода коэффициетов 
btnsolut = Button(windowdone , text = "Solute" ,command = click , fg = "black")
entryA = Entry(windowdone , width = 20)
entryB = Entry(windowdone , width = 20)
entryC = Entry(windowdone , width = 20)

#Создание заголовков для пунктов ввода 
labelA = Label(windowdone , text = "Коэффициент A")
labelB = Label(windowdone , text = "Коэффициент B")
labelC = Label(windowdone , text = "Коэффициент C")

#Создание пунктов для выдачи ответов 
labelD = Label(windowdone , text = "0")
labelDiz = Label(windowdone , text = "0")
labelx1 = Label(windowdone , text = "0")
labelx2 = Label(windowdone , text = "0")


#Создание заголовков для пунктов выдачи ответов 
labelDT = Label(windowdone , text = "Дискриминант")
labelDizT = Label(windowdone , text = "Корень из дискриминанта")
labelx1T = Label(windowdone , text = "Первый корень")
labelx2T = Label(windowdone , text = "Второй корень")

#Размещение заголовков для пунктов ввода
labelA.place(x=30 , y = 25)
labelB.place(x=230 , y = 25)
labelC.place(x=430 , y = 25)


#Размещение пунктов ввода 
entryA.place(x=30 , y = 50)
entryB.place(x=230 , y = 50)
entryC.place(x=430 , y = 50)




#Размещение заголовков для пунктов выдачи 
labelDT.place(x=30 , y = 100)
labelDizT.place(x=200 , y = 100)
labelx1T.place(x=400 , y = 100)
labelx2T.place(x=550 , y = 100)



#Размещение пунктов выдачи 
labelD.place(x=30 , y = 150)
labelDiz.place(x=200 , y = 150)
labelx1.place(x=400 , y = 150)
labelx2.place(x= 550 , y = 150)


#Размещение кнопки
btnsolut.place(x = 300 , y = 200)



windowdone.mainloop()
