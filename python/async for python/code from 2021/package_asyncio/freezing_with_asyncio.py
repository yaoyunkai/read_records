"""
@date: 2021-05-05
@author: liberty
@file: freezing_with_asyncio

the is a part of "project-demo"

"""
import asyncio
import tkinter as tk


class Form:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('500x300')
        self.root.title('MainWindow')

        self.button = tk.Button(self.root, text='开始计算', command=self.get_loop)
        self.label = tk.Label(master=self.root, text='等待计算结果')

        self.button.pack()
        self.label.pack()
        self.root.mainloop()

    async def calculate(self):
        await asyncio.sleep(3)
        self.label['text'] = 300

    def get_loop(self):
        self.loop = asyncio.get_event_loop()
        self.loop.run_until_complete(self.calculate())
        self.loop.close()


if __name__ == '__main__':
    form = Form()
