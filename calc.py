from tkinter import *
import tkinter.font as font

root = Tk()
root.geometry('370x420')
root.title("Simple Calculator")
p1 = PhotoImage(file='iconImg.png')
root.iconphoto(False, p1)

entry = Entry(root, width=37, bd=5, bg='black', fg='white')
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10, ipady=25)

# define Functions


def add():
    firstNumber=entry.get()
    global fNum
    global math
    math = 'addition'
    fNum = int(firstNumber)
    entry.delete(0,END)
    entry.insert(0, "{}+".format(firstNumber))


def sub():
    firstNumber = entry.get()
    global fNum
    global math
    math = 'subtraction'
    fNum = int(firstNumber)
    entry.delete(0, END)


def multiply():
    firstNumber = entry.get()
    global fNum
    global math
    math = 'multiplication'
    fNum = int(firstNumber)
    entry.delete(0, END)


def divide():
    firstNumber = entry.get()
    global fNum
    global math
    math = 'division'
    fNum = int(firstNumber)
    entry.delete(0, END)


def equal():
    # secondNum = entry.get()
    # entry.delete(0, END)
    # if math == 'addition':
    #     entry.insert(0, fNum + int(secondNum))
    # elif math == 'subtraction':
    #     entry.insert(0, fNum - int(secondNum))
    # elif math == 'multiplication':
    #     entry.insert(0, fNum * int(secondNum))
    # elif math == 'division':
    #     entry.insert(0, fNum / int(secondNum))
    global res
    global result
    res = entry.get()
    entry.delete(0, END)
    result = eval(res)
    entry.insert(0, result)



def button_click(n):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current)+str(n))


def button_clr():
    entry.delete(0, END)


def button_bksp():
    entry.delete(len(entry.get())-1)

# define buttons


myFont = font.Font(size=18)

button1 = Button(root, font=myFont, text='1', padx=20, pady=20, fg='white', bg='#12b886', command=lambda: button_click(1))
button2 = Button(root, font=myFont, text='2', padx=20, pady=20, fg='white', bg='#12b886', command=lambda: button_click(2))
button3 = Button(root, font=myFont, text='3', padx=20, pady=20, fg='white', bg='#12b886', command=lambda: button_click(3))
button4 = Button(root, font=myFont, text='4', padx=20, pady=20, fg='white', bg='#12b886', command=lambda: button_click(4))
button5 = Button(root, font=myFont, text='5', padx=20, pady=20, fg='white', bg='#12b886', command=lambda: button_click(5))
button6 = Button(root, font=myFont, text='6', padx=20, pady=20, fg='white', bg='#12b886', command=lambda: button_click(6))
button7 = Button(root, font=myFont, text='7', padx=20, pady=20, fg='white', bg='#12b886', command=lambda: button_click(7))
button8 = Button(root, font=myFont, text='8', padx=20, pady=20, fg='white', bg='#12b886', command=lambda: button_click(8))
button9 = Button(root, font=myFont, text='9', padx=20, pady=20, fg='white', bg='#12b886', command=lambda: button_click(9))
button0 = Button(root, font=myFont, text='0', padx=20, pady=20, fg='white', bg='#12b886', command=lambda: button_click(0))
buttonDec = Button(root, font=myFont, text='.', padx=22, pady=20, fg='white', bg='#12b886', command=lambda: button_click('.'))
buttonClr = Button(root, font=myFont, text='CE', padx=11, pady=20, fg='white', bg='#12b886', command=button_clr)
buttonBksp = Button(root, font=myFont, text='<-', padx=160, pady=20, fg='white', bg='#12b886', command=button_bksp)

buttonAdd = Button(root, font=myFont, text='+', fg='white', bg='#fd7e14', padx=17, pady=57, command=lambda: button_click('+'))
buttonSub = Button(root, font=myFont, text='-', fg='white', bg='#fd7e14', padx=25, pady=20, command=lambda: button_click('-'))
buttonDiv = Button(root, font=myFont, text='/', fg='white', bg='#fd7e14', padx=24, pady=20, command=lambda: button_click('/'))
buttonMul = Button(root, font=myFont, text='X', fg='white', bg='#fd7e14', padx=22, pady=20, command=lambda: button_click('*'))
buttonEqu = Button(root, font=myFont, text='=', fg='white', bg='#fd7e14', padx=20, pady=20, command=equal)
buttonBrOp = Button(root, font=myFont, text='(', fg='white', bg='#fd7e14', padx=25, pady=20, command=lambda: button_click('('))
buttonBrCl = Button(root, font=myFont, text=')', fg='white', bg='#fd7e14', padx=22, pady=20, command=lambda: button_click(')'))

# place buttons on screen

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

buttonDec.grid(row=4, column=0)
button0.grid(row=4, column=1)
buttonClr.grid(row=4, column=2)

buttonBrOp.grid(row=1, column=3)
buttonBrCl.grid(row=1, column=4)

buttonMul.grid(row=2, column=3)
buttonDiv.grid(row=2, column=4)

buttonSub.grid(row=3, column=3)
buttonAdd.grid(row=3, column=4, rowspan=2)
buttonEqu.grid(row=4, column=3)

buttonBksp.grid(row=5, column=0, columnspan=5)


root.mainloop()
