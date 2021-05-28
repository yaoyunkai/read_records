"""
@date: 2021-05-05
@author: liberty
@file: freezing_2

the is a part of "project-demo"

"""

import time
import tkinter as tk


class Form:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('500x300')
        self.root.title('MainWindow')

        self.button = tk.Button(self.root, text='开始计算', command=self.calculate)
        self.label = tk.Label(master=self.root, text='等待计算结果')

        self.button.pack()
        self.label.pack()
        self.root.mainloop()

    def calculate(self):
        time.sleep(3)
        self.label['text'] = 300


if __name__ == '__main__':
    form = Form()
