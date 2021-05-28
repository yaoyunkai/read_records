"""
@date: 2021-05-05
@author: liberty
@file: freezing_4

the is a part of "project-demo"

第一步：定义需要异步执行的一系列操作，及一系列协程函数；

第二步：在主线程中定义一个新的线程，然后在新线程中产生一个新的事件循环；

第三步：在主线程中，通过asyncio.run_coroutine_threadsafe(coroutine,loop)这个方法，将一系列异步方法注册到新线程的loop里面去，这样就是新线程负责事件循环的执行。


"""

import asyncio
import threading
import tkinter as tk  # 导入 Tkinter 库


class Form:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('500x300')
        self.root.title('窗体程序')  # 设置窗口标题

        self.button = tk.Button(self.root, text="开始计算", command=self.change_form_state)
        self.label = tk.Label(master=self.root, text="等待计算结果")

        self.button.pack()
        self.label.pack()

        self.root.mainloop()

    async def calculate(self):
        await asyncio.sleep(3)
        self.label["text"] = 300

    def get_loop(self, loop):
        self.loop = loop
        asyncio.set_event_loop(self.loop)
        self.loop.run_forever()

    def change_form_state(self):
        coroutine1 = self.calculate()
        new_loop = asyncio.new_event_loop()  # 在当前线程下创建时间循环，（未启用），在start_loop里面启动它
        t = threading.Thread(target=self.get_loop, args=(new_loop,))  # 通过当前线程开启新的线程去启动事件循环
        t.start()

        asyncio.run_coroutine_threadsafe(coroutine1, new_loop)  # 这几个是关键，代表在新线程中事件循环不断“游走”执行


if __name__ == '__main__':
    form = Form()
