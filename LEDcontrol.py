# my first app to control arduino with pyFirmata

from pyfirmata import Arduino, util
from tkinter import *
import time

board = Arduino('COM3')
iterator = util.Iterator(board)
iterator.start()

g = board.get_pin('d:6:o')  # Pin 6, digital output
r = board.get_pin('d:7:o')  # Pin 7, digital output
g.write(0)
r.write(0)


class Application(Frame):
    '''GUI app to controls LEDs'''

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        '''creats buttons and labels'''
        # Label with instruction
        Label(self, text='Push the button to turn on or off LED').grid(row=0, column=0, columnspan=3, sticky=W)

        # green LED label
        self.gLabel = Label(self, text='green LED is off')
        self.gLabel.grid(row=1, column=0, sticky=W)
        # green LED button
        self.gBtn = Button(self, text='Green LED', command=self.turnGreen)
        self.gBtn.grid(row=1, column=1, sticky=W)

        # red LED's label
        self.rLabel = Label(self, text='red LED is off')
        self.rLabel.grid(row=2, column=0, sticky=W)
        # red LED's button
        self.rBtn = Button(self, text='Red LED', command=self.turnRed)
        self.rBtn.grid(row=2, column=1, sticky=W)

        # exit button
        Button(self, text='Exit', command=self.exit).grid(row=3, column=3, sticky=W)

    def turnGreen(self):
        ''' turns on or off green LED'''
        if g.read() == 1:
            time.sleep(0.1)
            g.write(0)
            self.gLabel.configure(text='Green LED is off')
            self.gBtn.configure(bg='white')
        elif g.read() == 0:
            time.sleep(0.1)
            g.write(1)
            self.gLabel.configure(text='Green LED is on')
            self.gBtn.configure(bg='green')

    def turnRed(self):
        ''' turns on or off red LED'''
        if r.read() == 1:
            time.sleep(0.1)
            r.write(0)
            self.rLabel.configure(text='Red LED is off')
            self.rBtn.configure(bg='white')
        elif r.read() == 0:
            time.sleep(0.1)
            r.write(1)
            self.rLabel.configure(text='Red LED is on')
            self.rBtn.configure(bg='red')

    def exit(self):
        board.exit()
        root.destroy()


root = Tk()
root.title('LED control')
app = Application(root)
root.mainloop()

