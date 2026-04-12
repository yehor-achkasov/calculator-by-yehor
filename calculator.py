import tkinter as tk                                                    # import tkinter

root = tk.Tk()
root.title("calculator")
root.geometry("900x450")                                                # create a window

entry = tk.Entry(root, width=20)
entry.pack()                                                            # add entry line 

def add_symbol(symbol):
    entry.insert(tk.END, symbol) 

button1 = tk.Button(root, text='1', command=lambda: add_symbol('1')) 
button1.pack()  
           
button2 = tk.Button(root, text="2", command=lambda: add_symbol("2"))
button2.pack()

button3 = tk.Button(root, text="3", command=lambda: add_symbol("3"))
button3.pack()

button4 = tk.Button(root, text="4", command=lambda: add_symbol("4"))
button4.pack()

button5 = tk.Button(root, text="5", command=lambda: add_symbol("5"))
button5.pack()

button6 = tk.Button(root, text="6", command=lambda: add_symbol("6"))
button6.pack()

button7 = tk.Button(root, text='7', command=lambda: add_symbol('7'))
button7.pack()

button8 = tk.Button(root, text='8', command=lambda: add_symbol('8'))
button8.pack()

button9 = tk.Button(root, text="9", command=lambda: add_symbol('9'))
button9.pack()

button0 = tk.Button(root, text='0', command=lambda: add_symbol('0'))
button0.pack()                                                          #add defaulte symbols 



button_plus = tk.Button(root, text="+", command=lambda: add_symbol("+"))
button_plus.pack()

button_minus = tk.Button(root, text="-", command=lambda: add_symbol("-"))
button_minus.pack()

button_mul = tk.Button(root, text="*", command=lambda: add_symbol("*"))
button_mul.pack()

button_div = tk.Button(root, text="/", command=lambda: add_symbol("/"))
button_div.pack()                                                        #add operators                                                       

def calculate():
    expression = entry.get()
    result = eval(expression)
    entry.delete(0, tk.END)
    entry.insert(0, result) 
    
button_equal = tk.Button(root, text="=", command=calculate)
button_equal.pack()                                                      #add '='
  



root.mainloop()
