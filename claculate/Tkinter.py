import tkinter as tk

def press(touch_button):
    if touch_button == "C":
        display.delete(0, tk.END)
    elif touch_button == "=":
        try:
            result = eval(display.get())
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except Exception:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    else:
        display.insert(tk.END, touch_button)

root = tk.Tk()
root.title("Calculator")
root.resizable(False, False)

display = tk.Entry(root, font=("Arial", 24), justify="right", bd=8)
display.grid(row=0, column=0, columnspan=4, sticky="nsew")

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", "%", "=", "+",
    ".", ",", "X"
]

for i, key in enumerate(buttons):
    tk.Button(root, text=key, font=("Arial", 18), width=4, height=2,
              command=lambda k=key: press(k)).grid(row=i // 4 + 1, column=i % 4)

tk.Button(root, text="C", font=("Arial", 18), height=2,
          command=lambda: press("C")).grid(row=5, column=0, columnspan=4, sticky="nsew")

root.mainloop()
