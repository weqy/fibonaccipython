from tkinter import *

ws = Tk()
ws.title('fibonacci numbers python')
ws.geometry('400x300')

def welMsg(name):
    fib_terms = [0, 1]  # first two fibonacci terms

    user_input = int(name_Tf.get())

    # Add new fibonacci terms until the user_input is reached
    while fib_terms[-1] <= user_input:
        fib_terms.append(fib_terms[-1] + fib_terms[-2])

    if user_input in fib_terms:
        print(f'Yes. {user_input} is a fibonacci number.')
        Label(ws, text='Yes. ' + str(user_input) + ' is a fibonacci number.').pack(pady=50)
    else:
        print(f'No. {user_input} is NOT a fibonacci number.')
        Label(ws, text='No. ' + str(user_input) + ' is NOT a fibonacci number.').pack(pady=50)

Label(ws, text='Enter Number & hit enter key').pack(pady=50)
name_Tf = Entry(ws)
name_Tf.bind('<Return>',welMsg)
name_Tf.pack()

ws.mainloop()
