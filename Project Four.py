# Section 1
"""Essentially sets are what they are labeled at, collection of information of different subjects. Information on someone's background to what their credit card history is.
    The second one is an example that is really important as now of days this history is used to determine whether someone can be given certain privalges. Such as being lent money or being able to buy a house.
    Programmers may want information as in order to access these same privaleges. They themselves might not have a good spending history, thus rely on stealing someone else's identity to achieve their desires.
    They could find said information right off the bat by simply stalking someone's personal life on sociall media. Many people are connected throguh popular social medias, and if users have easy passwords on them, the likelyhood of that same password being on other apps is likely.
    Especially in older folk. They can hack, say Facebook, find the users Name, phone number, and email. And by stealing the address they can pretend to be the victim.
    But even then sometimes ordering or grouping data can help find certain items. There are apps now that people can use to store their account informations.
    While it may b e nice for older folk, it could easily be a problem. """


# Section 2
import tkinter as tk

root = tk.Tk()
root.title("Copying widget")

def copy_text():
    text_to_copy = entry.get()
    label.config(text=text_to_copy)

label = tk.Label(root, text="This is the current label")
label.pack()

# the box
entry = tk.Entry(root)
entry.pack()

# creating a button
button = tk.Button(root, text="Press to change", command=copy_text)
button.pack()

root.mainloop()


# the third section pops up when the first widget is closed
# Section 3

root = tk.Tk()
root.title("Finding the smallest number")
all_nums = []

def finder():
    values = [int(entry.get()) for entry in all_nums]
    small_num = min(values)
    label.config(text=f"Smallest Number: {small_num}")


for i in range(10):
    entry = tk.Entry(root, width=5)
    entry.pack(pady=5)
    all_nums.append(entry)

# just our label
label = tk.Label(root, text="Smallest Number: ")
label.pack(pady=10)

# the button the starts the 'calculations'
button = tk.Button(root, text="Find Smallest Number", command=finder)
button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
