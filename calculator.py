from tkinter import *
from tkinter import messagebox

FONT = ('Arial',16,'normal')
IS_OPERATION_SET = False
NUMB_COLOR = 'khaki'
OPER_COLOR = 'orange'

first_numb = ''
oper = ''
second_numb = ''

# ------------------- clearing the display
def clear_display():
    global first_numb, oper, second_numb,display_text, IS_OPERATION_SET
    display_text = ''
    first_numb = ''
    second_numb = ''
    oper = ''
    IS_OPERATION_SET = False
    canvas.itemconfig(display,text=display_text)

# ------------------- getting numbers -----------------------#
def press_numb(button_text):
    global first_numb
    global oper
    global display_text
    global second_numb
    if oper != '' and oper in display_text:
        second_numb += button_text
        display_text += button_text
        canvas.itemconfig(display,text=display_text)
    else:
        first_numb += button_text
        display_text += button_text
        canvas.itemconfig(display,text=display_text)
    return button_text

# ------------------- identifying operation -----------------#
def press_operation(operation):
    global oper, display_text, IS_OPERATION_SET
    if not IS_OPERATION_SET:
        display_text += operation
        IS_OPERATION_SET = True
    else:
        display_text = display_text.replace(oper,operation)
    oper = operation
    canvas.itemconfig(display,text=display_text)
    return operation

# -------------------- adding functionaloty to decimal separator button -------------------- #
def decimal_separator():
    global first_numb, oper, second_numb, display_text
    if display_text == '':
        first_numb += '0.'
        display_text += '0.'
        canvas.itemconfig(display,text=display_text)
    elif display_text[-1] == oper:
        display_text += '0.' 
        second_numb += '0.'
        canvas.itemconfig(display,text=display_text)
    else:
        if '.' not in first_numb:
            first_numb += '.'
            display_text += '.'
            canvas.itemconfig(display,text=display_text)
        if second_numb != '':
            if '.' not in second_numb:
                second_numb += '.'
                display_text += '.'
                canvas.itemconfig(display,text=display_text)


# ------------------- adding equal button functionality -------------#
def equal():
    global first_numb, oper, display_text,second_numb, IS_OPERATION_SET
    if first_numb != '' and oper != '' and second_numb !='':
        result = float(first_numb)
        if oper == '/' and second_numb == '0':
            display_text = first_numb + oper
            canvas.itemconfig(display,text=display_text)
            second_numb = ''
            messagebox.showerror(title='Zero Division error',message='You can not divide by zero. Please provide valid expression.')
            return None
        if oper == '+':
            result += float(second_numb)
        elif oper == '-':
            result -= float(second_numb)
        elif oper == '/' and second_numb != '0':
            result /= float(second_numb)
        elif oper == '*':
            result *= float(second_numb)
        if result % 1 == 0:
            display_text = str(int(result))
        else:
            display_text = str(round(result,6))
        canvas.itemconfig(display,text=display_text)
        first_numb = display_text
        second_numb = ''
        oper = ''
        IS_OPERATION_SET = False
    else:
        clear_display()
        messagebox.showerror(title='Invalid expression', message='Please provide valid expression.')
        

# ------------------- setting up UI----------------#
window = Tk()
window.config(bg='grey16')
window.title("Calculator")
window.config(pady=20, padx = 20)

canvas = Canvas(width=150, height=50,bg='grey26',highlightthickness=0)
display = canvas.create_text(75,25,text='',font=('Arial',20,'normal'),fill='light yellow')
canvas.grid(column=0,row=0,columnspan=4,sticky='EW',padx=10,pady=10)

display_text = canvas.itemcget(display,'text')

one = Button(text='1', font=FONT, background=NUMB_COLOR,width=3,height=2, command=lambda: press_numb('1'))
two = Button(text='2', font=FONT,background=NUMB_COLOR,width=3,height=2, command=lambda: press_numb('2'))
three = Button(text='3', font=FONT,background=NUMB_COLOR,width=3,height=2, command=lambda: press_numb('3'))
four = Button(text='4', font=FONT,background=NUMB_COLOR,width=3,height=2, command=lambda: press_numb('4'))
five = Button(text='5', font=FONT,background=NUMB_COLOR,width=3,height=2, command=lambda: press_numb('5'))
six = Button(text='6', font=FONT,background=NUMB_COLOR,width=3,height=2, command=lambda: press_numb('6'))
seven = Button(text='7', font=FONT,background=NUMB_COLOR,width=3,height=2, command=lambda: press_numb('7'))
eight = Button(text='8', font=FONT,background=NUMB_COLOR,width=3,height=2, command=lambda: press_numb('8'))
nine = Button(text='9', font=FONT,background=NUMB_COLOR,width=3,height=2, command=lambda: press_numb('9'))
zero = Button(text='0', font=FONT,background=NUMB_COLOR,width=3,height=2, command=lambda: press_numb('0'))

plus = Button(text='+',font=FONT,background=OPER_COLOR,width=3,height=2, command=lambda:press_operation('+'))
subtract = Button(text='-',font=FONT,background=OPER_COLOR,width=3,height=2, command=lambda:press_operation('-'))
multiply = Button(text='*',font=FONT,background=OPER_COLOR,width=3,height=2, command=lambda:press_operation('*'))
divide = Button(text='/',font=FONT,background=OPER_COLOR,width=3,height=2, command=lambda:press_operation('/'))

float_numb = Button(text='.',font=FONT,width=3,height=2,bg=OPER_COLOR, command=decimal_separator)
equal_button = Button(text='=',font=FONT,width=3,height=2,command=equal,bg=OPER_COLOR)
clear_button = Button(text='clear', font=FONT,bg=OPER_COLOR,command=clear_display)

equal_button.grid(column=0,row=5)
clear_button.grid(column=0,row=1,columnspan=4,sticky='EW')
float_numb.grid(column=2,row=5)
zero.grid(column=1,row=5)
one.grid(column=0,row=4)
two.grid(column=1,row=4)
three.grid(column=2,row=4)
four.grid(column=0,row=3)
five.grid(column=1,row=3)
six.grid(column=2,row=3)
seven.grid(column=0,row=2)
eight.grid(column=1,row=2)
nine.grid(column=2,row=2)
plus.grid(column=3,row=5)
subtract.grid(column=3,row=4)
multiply.grid(column=3,row=3)
divide.grid(column=3,row=2)





window.mainloop()
