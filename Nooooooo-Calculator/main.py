import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def on_button_click(value):
    current = str(entry.get())
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(value))

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
        messagebox.showerror("Error", "Invalid Input")

print("システム起動中です。しばらくお待ちください。")

app = tk.Tk()
app.title("Nooooooo 電卓")
app.geometry("370x285")
app.resizable(width=False, height=False)

style = ttk.Style()
style.theme_use('clam')

font_bold = ('Arial', 24, 'bold')

entry = ttk.Entry(app, font=font_bold, justify='right')
entry.grid(row=0, column=0, columnspan=4, ipady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    ttk.Button(app, text=button, width=8, command=lambda b=button: on_button_click(b) if b != '=' else calculate(),
               style='TButton').grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

ttk.Button(app, text='C', width=8, command=clear_entry, style='TButton').grid(row=row_val, column=col_val, padx=5, pady=5)

app.attributes("-alpha", 0.0)

for i in range(0, 101, 2):
    app.attributes("-alpha", i/100)
    app.update_idletasks()
    app.after(10)

print("システム起動が起動しました。\n\n"+
      "開発者: Nooooooo\n"+
      "このソフトを使用してもNoooooooは責任取りません。"
      )
app.mainloop()