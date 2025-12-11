import requests
import random
import tkinter as tk

# def submit_name():
#     global name
#     name = name_entry.get()
#     result_label.config(text=f" and now we go on {name}'s journey")

# root = tk.Tk()
# root.title("Name Input App")
# root.geometry("300x150")

# prompt_label = tk.Label(root, text="Enter your name:")
# prompt_label.pack(pady=5)

# name_entry = tk.Entry(root, width=2)
# name_entry.pack(pady=5)

# submit_button = tk.Button(root, text="Submit", command=submit_name)
# submit_button.pack(pady=5)

# result_label = tk.Label(root, text="")
# result_label.pack(pady=5)



# class character:
#     def __init__(self, mhp, exp, level):
#         self.mhp = int(mhp)
#         self.chp = int(mhp)
#         self.exp = int(exp)
#         self.level = int(level)
#         self.name = name
#         self.encounter()

#     def encounter(self):
#         label = tk.Label(root, text="You have encountered a")
#         label.pack(pady=7)



# Drake = character(20, 0, 1)
# Drake.__init__
# Drake.encounter

# root.mainloop()































'''
def submit_name():
    # Get the value from the entry widget
    global name
    name = name_entry.get()
    # Display the name in the label
    result_label.config(text=f" and now we go on {name}'s journey")

# Create the main window
root = tk.Tk()
root.title("Name Input App")
root.geometry("300x150")

# Create a label
prompt_label = tk.Label(root, text="Enter your name:")
prompt_label.pack(pady=5)

# Create an entry widget
name_entry = tk.Entry(root, width=25)
name_entry.pack(pady=5)

# Create a button to submit
submit_button = tk.Button(root, text="Submit", command=submit_name)
submit_button.pack(pady=5)

# Create a label to show the result
result_label = tk.Label(root, text="")
result_label.pack(pady=5)

# Run the application
root.mainloop()
'''

def Munster(mon):
    res = requests.get(f"https://api.open5e.com/monsters/{mon.lower}")

    if res.status_code != 200:
        print("Error fetching data!")
        return None

    data = res.json()
    return {
        "name": data("Name"),
    }
m = Munster("Aboleth")
print(m)
