import tkinter as tk

def click_button(button_text):
    text_1 = entry.get()
    if button_text == "=":
        try:
            result = eval(text_1)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

root = tk.Tk()
root.title("calculator")

entry = tk.Entry(root, width=25, font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'
]

row = 1
col = 0
for button_text in buttons:
    btn = tk.Button(root, text=button_text, width=5, height=2, font=("Arial", 12),bg='orange',fg='black',
                    command=lambda button_text=button_text: click_button(button_text))
    btn.grid(row=row, column=col, padx=5, pady=5,)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()