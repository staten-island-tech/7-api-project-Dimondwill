import requests
import random
import tkinter as tk

'''
def submit_name():
    # Get the value from the entry widget
    name = name_entry.get()
    # Display the name in the label
    result_label.config(text=f"Hello, {name}! we shall now start your wizarding journy;")

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
    res = requests.get(f"https://api.open5e.com/v2/creatures/{mon.lower}")

    if res.status_code != 200:
        print("Error fetching data!")
        return None

    data = res.json()
    return {
        "name": data("name"),
        "key": data["key"],
        "url": data["url"]
    }
m = Munster("Aboleth")
print(m)