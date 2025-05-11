import tkinter as tk

root = tk.Tk()
root.geometry("500x500")
root.title("Hello Baby")
label = tk.Label(root, text="Hello World!")
label.pack(pady=20)
def gay():
   print("gay homo gay")
button = tk.Button(root, text="gay button", command=lambda: gay())
button.pack(pady = 50)

root.mainloop()