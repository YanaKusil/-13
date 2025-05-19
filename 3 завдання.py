import tkinter as tk
from math import sin

def calculate_expression(event=None):
    try:
        x = float(entry_x.get())
        k = float(entry_k.get())

        result = (sin(2 * k * x) + 0.2) / (2 * k + 5)
        format_result = "{:.2f}".format(result)
        label_result.config(text="Результат: " + format_result)

    except Exception as e:
        label_result.config(text="Помилка: " + str(e))

root = tk.Tk()
root.title("Обчислення виразу")
root.geometry("400x300")

try:
    photo = tk.PhotoImage(file="lb13ph3.gif")
    label_image = tk.Label(root, image=photo)
    label_image.grid(row=0, column=0, columnspan=2, pady=10)
except:
    label_image = tk.Label(root, text="[Зображення не знайдено]")
    label_image.grid(row=0, column=0, columnspan=2, pady=10)

# Введення x
label_x = tk.Label(root, text="Введіть x:")
label_x.grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_x = tk.Entry(root)
entry_x.grid(row=1, column=1, padx=5, pady=5)

# Введення k
label_k = tk.Label(root, text="Введіть k:")
label_k.grid(row=2, column=0, padx=5, pady=5, sticky="e")
entry_k = tk.Entry(root)
entry_k.grid(row=2, column=1, padx=5, pady=5)

# Кнопка
button_calc = tk.Button(root, text="Обчислити", command=calculate_expression)
button_calc.grid(row=3, column=0, columnspan=2, pady=10)

# Результат
label_result = tk.Label(root, text="", fg="blue")
label_result.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()