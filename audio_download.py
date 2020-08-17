import tkinter as tk


mainWindow = tk.Tk()

mainWindow.title("音乐下载")
mainWindow.geometry('560x450')

# 标签
label = tk.Label(mainWindow, text="请输入下载歌曲：", font=('宋体', 20))
label.grid()

# 输入框
entry = tk.Entry(mainWindow, font=('宋体', 20))
entry.grid(row=0, column=1)

# 列表框
listbox = tk.Listbox(mainWindow, font=('', 15), width=55, heigh=16)
listbox.grid(row=1, columnspan=2)

# 下载按钮
button1 = tk.Button(mainWindow, text='下载', font=('宋体', 15))
button1.grid(row=2, column=0, sticky=tk.W)

button2 = tk.Button(mainWindow, text='退出', font=('宋体', 15))
button2.grid(row=2, column=1, sticky=tk.E)

# 显示界面
mainWindow.mainloop()
