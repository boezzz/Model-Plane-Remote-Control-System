from tkinter import *

class PFD:
    def __init__(self, master, height, width):
        self.frame = Frame(master = master, height = height, width = width, bg = "black")
        self.frame.pack()

if __name__ == "__main__":
    root = Tk()
    root.geometry("300x400")
    PFD(root, 200, 200)

    root.mainloop()
    