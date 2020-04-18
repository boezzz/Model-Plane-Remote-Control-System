from math import sin, cos, pi

from threading import Thread
from time import sleep
from tkinter import *
class Engine:
    def __init__(self, master, length, pack_side):
        self.length = length
        self.frame = Frame(master = master, width = length, height = length, bg = "black")
        
        self.arc = Canvas(self.frame, width = length, height = length, bg = "black", bd = 0, highlightthickness = 0)
        self.arc.create_arc(5, 5, length - 5, length - 5, start = 0, extent = 225, style = ARC, outline = "white", width = 2)
        self.arc.create_rectangle(0.5 * length, 0.6 * length, 0.9 * length, 0.9 * length, outline = "white", width = 2)
        self.arc.pack()
        self.frame.pack(side = pack_side, fill = "both")
        self.r = length / 2 - 5
        self.center = (int(length / 2), int(length / 2))


    def turn_on(self, val_min, val_max):
        self.val = 0
        self.val_max = val_max
        self.val_min = val_min
        self.text_color = "green"
        self.arc.create_text(0.25 * self.length, 0.8 * self.length, text = str(val_min), fill = "white", font=("Menlo", int(self.length / 15)))
        self.arc.create_text(0.9 * self.length, 0.55 * self.length, text = str(val_max), fill = "white", font=("Menlo", int(self.length / 15)))
        # self.text = self.arc.create_text(0.75 * self.length, 0.8 * self.length, text = str(self.val), fill = self.text_color)
        self.text = self.arc.create_text(0.7 * self.length, 0.75 * self.length, text = "", fill = self.text_color, font = ("Menlo", int(self.length / 15)))
        self.pointer = self.arc.create_line(self.center, (self._val2pos(0)[0] + self.center[0], self.length - (self._val2pos(0)[1] + self.center[1])), fill = "green", width = 3)
        self.arc.pack()

    def change_to(self, val):

        self.val = val
        self.arc.coords(self.pointer, self.center[0], self.center[1], self._val2pos(val)[0] + self.center[0], self.length - (self._val2pos(val)[1] + self.center[1]))
        self.arc.itemconfig(self.text, text = str(val))
        self.arc.pack()

    def _val2pos(self, val):
        return (
            int(cos((self.val_max - val) / (self.val_max - self.val_min) * (5/4) * pi) * self.r),
            int(sin((self.val_max - val) / (self.val_max - self.val_min) * (5/4) * pi) * self.r)
        )

if __name__ == "__main__":
    print(__name__)
    root = Tk()
    root.geometry("800x400")
    root.configure(bg = "black")
    E_1 = Engine(root, 400, "left")
    E_2 = Engine(root, 400, "right")
    def turn_on():
        sleep(5)
        E_1.turn_on(0, 100)
        for i in range(0, 101):
            E_1.change_to(i)
            sleep(0.01)
    t = Thread(target = turn_on, args = ())
    t.start()
    root.mainloop()
    