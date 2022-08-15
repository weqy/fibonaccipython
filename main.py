import tkinter as tk # gui
from tkinter import * # all necessary tkinter commands

ws = tk.Tk() # canvas
ws.title('fibonacci numbers python') # canvas title

canvas1 = tk.Canvas(width = 400, height = 300) # canvas height and width
canvas1.pack() # create canvas

name_Tf = tk.Entry(ws) # create entry
name_Tf.bind('<Return>', (lambda event: welMsg())) # function is called when enter is pressed
canvas1.create_window(200, 140, window=name_Tf) # shows entry in canvas

instructions = tk.Label(ws, text='Enter Number') # instructions for user
canvas1.create_window(200, 110, window=instructions) # show instructions

ws.btn = tk.Button(ws, text = 'Enter', bd = '5', command= (lambda: welMsg())) # create button that runs welMsg
canvas1.create_window(200, 180, window=ws.btn) # show button

def create_canvas(): # define function
    canvas1.delete("all")  # delete everything in canvas
    instructions = tk.Label(ws, text='Enter Number')  # instructions for user
    canvas1.create_window(200, 110, window=instructions)  # show instructions

    ws.btn = tk.Button(ws, text='Enter', bd='5', command=(lambda: welMsg()))  # create button that runs welMsg
    canvas1.create_window(200, 180, window=ws.btn)  # show button
    canvas1.create_window(200, 140, window=name_Tf)

def create_entry(): # define function
    name_Tf = tk.Entry(ws)  # create entry
    name_Tf.bind('<Return>', (lambda event: welMsg()))  # function is called when enter is pressed

def clear_text(): # define function
   name_Tf.delete(0, END) # deletes entry from first symbol to end

def welMsg(): # define function
    fib_terms = [0, 1]  # first two fibonacci terms

    user_input = int(name_Tf.get()) # converts entry value to int
    create_canvas()

    # add new fibonacci terms until the user_input is reached
    while fib_terms[-1] <= user_input: # add new elements until it is equal to the user input-1
        fib_terms.append(fib_terms[-1] + fib_terms[-2]) #

    if user_input in fib_terms: # entry get is found in list
        result = tk.Label(ws, text='Yes. ' + str(user_input) + ' is a fibonacci number.') # print result & entry value to canvas

    else: # entry get is not found in list
        result = tk.Label(ws, text='No. ' + str(user_input) + ' is NOT a fibonacci number.') # print result & entry value to canvas
        result2= tk.Label(ws, text='The closest lower fibonacci number is ' + str(fib_terms[-2])) # last 2 fibonacci numbers in list
        canvas1.create_window(200, 230, window=result2) # shows result2 in canvas
    canvas1.create_window(200, 200, window=result) # show result in canvas
    create_entry() # creates new entry
    clear_text() # clears entry text


ws.mainloop() # run tkinter event loop
