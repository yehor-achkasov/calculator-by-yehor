import tkinter as tk      # import tkinter

root = tk.Tk()
root.title("calculator")
root.geometry("300x250")  # create a window

entry=tk.Entry(root, width=30)
entry.grid(row=0, column=0, columnspan=4)          # add entry

def add_symbol(symbol):
    entry.insert(tk.END, symbol) 


def calculate():
    expression = entry.get()
    result = eval(expression)
    entry.delete(0, tk.END)
    entry.insert(0, result) 


tk.Button(root, text="7", command=lambda: add_symbol("7")).grid(row=1, column=0)
tk.Button(root, text="8", command=lambda: add_symbol("8")).grid(row=1, column=1)
tk.Button(root, text="9", command=lambda: add_symbol("9")).grid(row=1, column=2)
tk.Button(root, text="/", command=lambda: add_symbol("/")).grid(row=1, column=3)
tk.Button(root, text='4', command=lambda: add_symbol('4')).grid(row=2, column=0)
tk.Button(root, text='5', command=lambda: add_symbol('5')).grid(row=2, column=1)
tk.Button(root, text='6', command=lambda: add_symbol('6')).grid(row=2, column=2)
tk.Button(root, text='*', command=lambda: add_symbol('*')).grid(row=2, column=3)
tk.Button(root, text='1', command=lambda: add_symbol('1')).grid(row=3, column=0)
tk.Button(root, text='2', command=lambda: add_symbol('2')).grid(row=3, column=1)
tk.Button(root, text='3', command=lambda: add_symbol('3')).grid(row=3, column=2)
tk.Button(root, text='+', command=lambda: add_symbol('+')).grid(row=3, column=3)
tk.Button(root, text='0', command=lambda: add_symbol('0')).grid(row=4, column=0)
tk.Button(root, text='-', command=lambda: add_symbol('-')).grid(row=4, column=1)
tk.Button(root, text='=', command=calculate).grid(row=4, column=2)

def clear():
    entry.delete(0, tk.END) 

tk.Button(root, text='C', command=clear).grid(row=4, column=3)




root.mainloop()
