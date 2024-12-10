import tkinter as tk


root = tk.Tk()
root.title("Compound Interest Calculator - Main")
root.geometry("500x400")

principal_label = tk.Label(root, text="Principal: ")
principal_label.pack()

principal_entry = tk.Entry(root)
principal_entry.pack()

currency_label = tk.Label(root, text="Currency: ")
currency_label.pack()

currency_entry = tk.Entry(root)
currency_entry.pack()

interestrate_label = tk.Label(root, text="Interest (%): ")
interestrate_label.pack()

interestrate_entry = tk.Entry(root)
interestrate_entry.pack()

time_label = tk.Label(root, text="Time: ")
time_label.pack()

time_entry = tk.Entry(root)
time_entry.pack()

def on_click():
    principal = int(principal_entry.get())
    currency = currency_entry.get()
    interest = int(interestrate_entry.get())
    time = int(time_entry.get())

    future_value = int(principal*((1+(interest/100))**time))

    calculation = tk.Toplevel(root)
    calculation.title("Compound Interest Calculator - Calculation")
    calculation.geometry("400x300")

    futurevalue_label = tk.Label(calculation, text="The total amount after " + str(time) + " year(s) is " + str(future_value) + " " + currency + ".")
    futurevalue_label.pack(pady=20)

    yd = future_value - principal
    yd_label = tk.Label(calculation, text="Yield: " + str(yd) + " " + currency)
    yd_label.pack(pady=20)

button = tk.Button(root, text="Calculate", command=on_click)
button.pack()

root.mainloop()
