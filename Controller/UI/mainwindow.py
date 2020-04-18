from tkinter import *

class mainWindow:
    def __init__(self, geometry):
        self.mainwindow = Tk()
        self.mainwindow.geometry(geometry)
        self.mainwindow.configure(background ="#000000")

    def add_frame(self, frame):
        pass

if __name__ == "__main__":
    MW = mainWindow("300x400")