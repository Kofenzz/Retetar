import tkinter as tk

# Crearea ferestrei

root = tk.Tk()
root.title("Retetar")

# Eticheta

label = tk.Label(root, text = "Bun venit in Retetar!")
label.pack


# Crearea unui buton de callback
def button_callback():
    print("Merge")

# Creare buton
button = tk.Button(root,text="Click ", command=button_callback())
button.pack

# Dai bataie

root.mainloop()