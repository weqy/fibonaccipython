import tkinter as tk
from tkinter import * # all necessary tkinter commands
import time

ws = tk.Tk() # canvas
ws.title('fibonacci numbers python') # canvas title
#ws.geometry('400x300') # canvas height and width

canvas1 = tk.Canvas(width = 400, height = 300)
canvas1.pack()

name_Tf = tk.Entry(ws) # create entry
name_Tf.bind('<Return>', (lambda event: welMsg())) # function is called when enter is pressed
canvas1.create_window(200, 140, window=name_Tf)

instructions = tk.Label(ws, text='Enter Number & hit enter key') # instructions for user
canvas1.create_window(200, 110, window=instructions)

ws.btn = tk.Button(ws, text = 'Enter', bd = '5', command= (lambda: welMsg()))
canvas1.create_window(200, 180, window=ws.btn)

def welMsg(): # define function
    fib_terms = [0, 1]  # first two fibonacci terms

    user_input = int(name_Tf.get()) # converts entry value to int

    # add new fibonacci terms until the user_input is reached
    while fib_terms[-1] <= user_input: # add new elements until it is equal to the user input-1
        fib_terms.append(fib_terms[-1] + fib_terms[-2]) #

    if user_input in fib_terms: # entry get is found in list
        result = tk.Label(ws, text='Yes. ' + str(user_input) + ' is a fibonacci number.') # print result & entry value to canvas
        canvas1.create_window(200, 200, window=result)

    else: # entry get is not found in list
        result = tk.Label(ws, text='No. ' + str(user_input) + ' is NOT a fibonacci number.') # print result & entry value to canvas
        canvas1.create_window(200, 200, window=result)
        result2= tk.Label(ws, text='The closest lower fibonacci number is ' + str(fib_terms[-2]))
        canvas1.create_window(200, 230, window=result2)


ws.mainloop() # run tkinter event loop
