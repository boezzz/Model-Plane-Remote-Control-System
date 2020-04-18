from tkinter import *
from time import sleep
from threading import Thread

class rollBar:
    def __init__(self, master, width, height, LoR):
        self.LoR = LoR
        self.frame = Frame(master = master, width = width, height = height, bg = "black")
        self.frame.pack()
        self.canvas = Canvas(self.frame, width = width, height = height, bg = "grey", bd = 0, highlightthickness = 0)
        self.canvas.pack()
        self.width = width
        self.height = height
        self.div_len = height / 4
        self.lines = []
        self.numbers = []
        if LoR == "L":
            self.canvas.create_rectangle(10, int(self.height / 2) + 6, self.width - 1, int(self.height / 2) - 6, outline = "white", fill = "black")
        elif LoR == "R":
            self.canvas.create_rectangle(0, int(self.height / 2) + 6, self.width - 11, int(self.height / 2) - 6, outline = "white", fill = "black")

    def turn_on(self, div):
        self.div = div
        if self.LoR == "L":
            self.canvas.create_polygon(10, int(self.height / 2) + 6, 10, int(self.height / 2) - 6, 0, int(self.height / 2), fill = "white")
        elif self.LoR == "R":
            self.canvas.create_polygon(self.width - 11, int(self.height / 2) + 6, self.width - 11, int(self.height / 2) - 6, self.width - 1, int(self.height / 2), fill = "white")
        self.change_to(0)
        

    def change_to(self, val):
        # del lines and numbers
        for line in self.lines:
            self.canvas.delete(line)
        self.lines = []
        for number in self.numbers:
            self.canvas.delete(number)
        self.lines = []

        # draw lines and numbers
        delta_h = (val % self.div) * (self.div_len / self.div)
        y = int(self.height / 2 + delta_h)
        y_val = val - (val % self.div)

        delta_y = 0
        delta_y_val = 0

        if self.LoR == "L":
            while delta_y + y < self.height:
                self.lines.append(self.canvas.create_line((0, y + delta_y), (int(self.width / 2), y + delta_y), fill = "white", width = 2))
                self.numbers.append(self.canvas.create_text(self.width * 0.75, y + delta_y, text = str(y_val - delta_y_val), fill = "white", font=("Menlo", int(self.width / 5))))
                dd_y = 0
                while delta_y + y + dd_y < self.height and dd_y < self.div_len:
                    self.lines.append(self.canvas.create_line((0, y + delta_y + dd_y), (int(self.width / 4), y + delta_y + dd_y), fill = "white", width = 1))
                    dd_y += int(self.div_len / 5)
                delta_y += self.div_len
                delta_y_val += self.div

            delta_y = 0
            # delta_y = self.div_len
            delta_y_val = 0
            # delta_y_val = self.div

            while y - delta_y >= 0:
                self.lines.append(self.canvas.create_line((0, y - delta_y), (int(self.width / 2), y - delta_y), fill = "white", width = 2))
                self.numbers.append(self.canvas.create_text(int(self.width * 0.75), y - delta_y, text = str(y_val + delta_y_val), fill = "white", font=("Menlo", int(self.width / 5))))
                dd_y = 0
                while y - delta_y - dd_y >= 0 and dd_y < self.div_len:
                    self.lines.append(self.canvas.create_line((0, y - delta_y - dd_y), (int(self.width / 4), y - delta_y - dd_y), fill = "white", width = 1))
                    dd_y += int(self.div_len / 5)
                delta_y += self.div_len
                delta_y_val += self.div
            
            self.canvas.create_rectangle(10, int(self.height / 2) + 6, self.width - 1, int(self.height / 2) - 6, outline = "white", fill = "black")
            self.canvas.create_text(int((self.width - 10) / 2) + 10, int(self.height / 2), text = str(val), fill = "white", font=("Menlo", int(self.width / 5 + 1)))
            self.canvas.pack()

        elif self.LoR == "R":

            while delta_y + y < self.height:
                self.lines.append(self.canvas.create_line((self.width - 1, y + delta_y), (int(self.width / 2), y + delta_y), fill = "white", width = 2))
                self.numbers.append(self.canvas.create_text(self.width * 0.25, y + delta_y, text = str(y_val - delta_y_val), fill = "white", font=("Menlo", int(self.width / 5))))
                dd_y = 0
                while delta_y + y + dd_y < self.height and dd_y < self.div_len:
                    self.lines.append(self.canvas.create_line((self.width - 1, y + delta_y + dd_y), (int(self.width / 4 * 3), y + delta_y + dd_y), fill = "white", width = 1))
                    dd_y += int(self.div_len / 5)
                delta_y += self.div_len
                delta_y_val += self.div

            delta_y = 0
            # delta_y = self.div_len
            delta_y_val = 0
            # delta_y_val = self.div

            while y - delta_y >= 0:
                self.lines.append(self.canvas.create_line((self.width - 1, y - delta_y), (int(self.width / 2), y - delta_y), fill = "white", width = 2))
                self.numbers.append(self.canvas.create_text(int(self.width * 0.25), y - delta_y, text = str(y_val + delta_y_val), fill = "white", font=("Menlo", int(self.width / 5))))
                dd_y = 0
                while y - delta_y - dd_y >= 0 and dd_y < self.div_len:
                    self.lines.append(self.canvas.create_line((self.width - 1, y - delta_y - dd_y), (int(self.width / 4 * 3), y - delta_y - dd_y), fill = "white", width = 1))
                    dd_y += int(self.div_len / 5)
                delta_y += self.div_len
                delta_y_val += self.div
            
            self.canvas.create_rectangle(0, int(self.height / 2) + 6, self.width - 11, int(self.height / 2) - 6, outline = "white", fill = "black")
            self.canvas.create_text(int((self.width - 10) / 2) + 10, int(self.height / 2), text = str(val), fill = "white", font=("Menlo", int(self.width / 5 + 1)))
            self.canvas.pack()            

        

if __name__ == "__main__":
    root = Tk()
    root.geometry("50x300")
    R = rollBar(root, 50, 300, "R")
    def c_c():
        sleep(1)
        R.turn_on(100)
        for i in range(500):
            R.change_to(i)
            sleep(0.01)
    t = Thread(target = c_c, args = ())
    t.start()
    root.mainloop()