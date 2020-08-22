import os
from urllib.request import urlretrieve
import tkinter as tk
import requests
import jsonpath


def song_load(listbox, url, title):
    os.makedirs("音乐下载", exist_ok=True)
    path = "音乐下载\\{}.mp3".format(title)
    listbox.insert(tk.END, '歌曲: {}，正在下载...'.format(title))
    listbox.see(tk.END)
    listbox.update()

    urlretrieve(url, path)

    listbox.insert(tk.END, '歌曲: {}，下载完毕'.format(title))
    listbox.see(tk.END)
    listbox.update()


def get_music_name(listbox, entry):
    name = entry.get()
    headers = {
        'X-Requested-With': 'XMLHttpRequest'
    }

    params = {
        'input': name,
        'filter': 'name',
        'type': 'qq',
        'page': 1,
    }
    url = 'http://www.youtap.xin/'
    resp = requests.post(url, data=params, headers=headers)
    data = resp.json()
    title = jsonpath.jsonpath(data, "$..title")[0]
    # author = jsonpath.jsonpath(data, "$..author")[0]
    url = jsonpath.jsonpath(data, "$..url")[0]

    # print(title)
    # print(author)
    # print(url)
    song_load(listbox, url, title)


# get_music_name()

def display():
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
    button1 = tk.Button(mainWindow, text='下载', font=('宋体', 15), command=lambda:get_music_name(listbox, entry))
    button1.grid(row=2, column=0, sticky=tk.W)

    button2 = tk.Button(mainWindow, text='退出', font=('宋体', 15), command=mainWindow.quit)
    button2.grid(row=2, column=1, sticky=tk.E)

    # 显示界面
    mainWindow.mainloop()

if __name__ == '__main__':
    display()

