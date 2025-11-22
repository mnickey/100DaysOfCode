from tkinter import *

def button_clicked():
    print("Button clicked")
    # my_label.config(text="Button clicked")
    result_label.config(text=f"{int(input.get()) / 1.609:.2f}")


window = Tk()
window.title("GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
miles_label = Label(text="Miles", font=("Arial", 18, "bold"))
is_equal_to_label = Label(text="is equal to", font=("Arial", 18, "bold"))
km_label = Label(text="Km", font=("Arial", 18, "bold"))
result_label = Label(text="0", font=("Arial", 18, "bold"))
# my_label["text"] = "New Label"
# my_label.config(text="New Text")
# my_label.pack()
# my_label.place(x=100, y=100)
miles_label.grid(row=0, column=2)
is_equal_to_label.grid(row=1, column=0)
km_label.grid(row=1, column=3)
result_label.grid(row=1, column=1)

# Button
button = Button(text="Calculate", command=button_clicked)
# button.pack()
button.grid(row=2, column=1)

# Entry
input = Entry(width=10)
print(input.get()) # will do nothing, need to tie to the button_clicked function
# input.pack()
input.grid(row=0, column=1)

window.mainloop()
