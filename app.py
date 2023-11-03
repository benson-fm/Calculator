from tkinter import *
# from tkinter import ttk
import ttkbootstrap as ttk

# Global Vars
global cmd
global ans
global first

# Declarations
first = True
ans = 0

# Functions
def addNum(num):
    x = str(view_var.get()) + str(num)
    view_var.set(int(x))
    l_ANS['text'] = view_var.get()

def delete():
    num = str(view_var.get())
    if len(num) == 1:
        view_var.set(0)
    else:    
        view_var.set(int(num[0:-1]))
    l_ANS['text'] = view_var.get()

def plus():
    global cmd
    global ans
    cmd = 0
    ans += view_var.get()
    view_var.set(0)
    l_ANS['text'] = 0

def minus():
    global cmd
    global ans
    global first
    cmd = 1
    if first == True:
        ans += view_var.get()
        first = False
    else:
        ans -= view_var.get()
    view_var.set(0)
    l_ANS['text'] = 0

def mul():
    global cmd
    global ans
    global first
    cmd = 2
    print(first)
    if first == True:
        ans += view_var.get()
        first = False
    else:
        ans *= view_var.get()
    view_var.set(0)
    l_ANS['text'] = 0

def div():
    global cmd
    global ans
    global first
    cmd = 3
    if first == True:
        ans += view_var.get()
        first = False
    else:
        ans /= view_var.get()
    view_var.set(0)
    l_ANS['text'] = 0

def equals():
    global ans
    global first
    if cmd == 0:
        ans += view_var.get()
        l_ANS['text'] = ans
        view_var.set(0)
        ans = 0
    elif cmd == 1:
        ans -= view_var.get()
        l_ANS['text'] = ans
        view_var.set(0)
        ans = 0
        first = True
    elif cmd == 2:
        ans *= view_var.get()
        l_ANS['text'] = ans
        view_var.set(0)
        ans = 0
        first = True
    elif cmd == 3:
        ans /= view_var.get()
        l_ANS['text'] = (ans)
        view_var.set(0)
        ans = 0
        first = True
   
# Intials
window = Tk()
window.geometry('420x525')
window.title('Calculator')
s = ttk.Style()
content = ttk.Frame(window)
s.theme_use('cosmo')
print(s.theme_names())

# vars 
view_var = IntVar(value = 0)

# layout
content.grid(column=0, row = 0)
l_ANS = ttk.Label(content, text = view_var.get(), font = 'Arial 36')
b_1 = ttk.Button(content, text = '1', command = lambda: addNum(1))
b_2 = ttk.Button(content, text = '2', command = lambda: addNum(2))
b_3 = ttk.Button(content, text = '3', command = lambda: addNum(3))
b_4 = ttk.Button(content, text = '4', command = lambda: addNum(4))
b_5 = ttk.Button(content, text = '5', command = lambda: addNum(5))
b_6 = ttk.Button(content, text = '6', command = lambda: addNum(6))
b_7 = ttk.Button(content, text = '7', command = lambda: addNum(7))
b_8 = ttk.Button(content, text = '8', command = lambda: addNum(8))
b_9 = ttk.Button(content, text = '9', command = lambda: addNum(9))
b_0 = ttk.Button(content, text = '0', command = lambda: addNum(0))
b_plus = ttk.Button(content, text = '+', command = plus)
b_minus = ttk.Button(content, text = '-', command = minus)
b_multiply = ttk.Button(content, text = '*', command = mul)
b_divide = ttk.Button(content, text = '/', command = div)
b_equals = ttk.Button(content, text = '=', command = equals)
b_delete = ttk.Button(content, text = 'del', command = delete)
# Future Buttons
# b_point = ttk.Button(content, text = '.', command = point)
# b_negative = ttk.Button(content, text = '+/-', command = negative)
# b_exponent = ttk.Button(content, text = '+/-', command = exponent)
# b_squart = ttk.Button(content, text = '+/-', command = squart)
# b_prevANS = ttk.Button(content, text = 'ans', command = ans)

# # placement
# content.grid(column = 0, row = 0)
# l_ANS.grid(column = 0, row = 0, columnspan = 5, rowspan = 2, sticky = (S,E))
# b_1.grid(column = 0, row = 2, sticky = (N, S, E, W))
# b_2.grid(column = 1, row = 2, sticky = (N, S, E, W))
# b_3.grid(column = 2, row = 2, sticky = (N, S, E, W))
# b_4.grid(column = 0, row = 3, sticky = (N, S, E, W))
# b_5.grid(column = 1, row = 3, sticky = (N, S, E, W))
# b_6.grid(column = 2, row = 3, sticky = (N, S, E, W))
# b_7.grid(column = 0, row = 4, sticky = (N, S, E, W))
# b_8.grid(column = 1, row = 4, sticky = (N, S, E, W))
# b_9.grid(column = 2, row = 4, sticky = (N, S, E, W))
# b_0.grid(column = 3, row = 4, sticky = (N, S, E, W))
# b_equals.grid(column = 3, row = 3, sticky = (N, S, E, W))
# b_delete.grid(column = 3, row = 2, sticky = (N, S, E, W))
# b_plus.grid(column = 0, row = 5, sticky = (N, S, E, W))
# b_minus.grid(column = 1, row = 5, sticky = (N, S, E, W))
# b_multiply.grid(column = 2, row = 5, sticky = (N, S, E, W))
# b_divide.grid(column = 3, row = 5, sticky = (N, S, E, W))

l_ANS.grid(column = 0, row = 0, columnspan = 5, rowspan = 2, sticky = (S,E), ipady = 40)
b_1.grid(column = 0, row = 2, ipadx = 35, ipady = 35, sticky = (N, S, E, W))
b_2.grid(column = 1, row = 2, ipadx = 35, ipady = 35, sticky = (N, S, E, W))
b_3.grid(column = 2, row = 2, ipadx = 35, ipady = 35, sticky = (N, S, E, W))
b_4.grid(column = 0, row = 3, ipadx = 35, ipady = 35, sticky = (N, S, E, W))
b_5.grid(column = 1, row = 3, ipadx = 35, ipady = 35, sticky = (N, S, E, W))
b_6.grid(column = 2, row = 3, ipadx = 35, ipady = 35, sticky = (N, S, E, W))
b_7.grid(column = 0, row = 4, ipadx = 35, ipady = 35, sticky = (N, S, E, W))
b_8.grid(column = 1, row = 4, ipadx = 35, ipady = 35, sticky = (N, S, E, W))
b_9.grid(column = 2, row = 4, ipadx = 35, ipady = 35, sticky = (N, S, E, W))
b_0.grid(column = 3, row = 4, ipadx = 35, ipady = 35, sticky = (N, S, E, W))
b_equals.grid(column = 3, row = 3, ipadx = 35, ipady = 35, sticky = (N, S, E, W))
b_delete.grid(column = 3, row = 2, ipadx = 35, ipady = 35, sticky = (N, S, E, W))
b_plus.grid(column = 0, row = 5, ipadx = 35, ipady = 35, sticky = (N, S, E, W))
b_minus.grid(column = 1, row = 5, ipadx = 35, ipady = 35, sticky = (N, S, E, W))
b_multiply.grid(column = 2, row = 5, ipadx = 35, ipady = 35, sticky = (N, S, E, W))
b_divide.grid(column = 3, row = 5, ipadx = 35, ipady = 35, sticky = (N, S, E, W))

# Scalability
window.columnconfigure(0, weight = 1)
window.rowconfigure(0, weight = 1)
content.columnconfigure(0, weight = 1)
content.columnconfigure(1, weight = 1)
content.columnconfigure(2, weight = 1)
content.columnconfigure(3, weight = 1)
content.rowconfigure(0, weight = 2)
content.rowconfigure(1, weight = 2)
content.rowconfigure(2, weight = 1)


window.mainloop()

