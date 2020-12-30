from tkinter import ttk, messagebox

import easygui
from moviepy.editor import *
from tkinter import *

window = Tk()
window['bg'] = "#59566e"
window.title("Delete_audio")
window.geometry("300x230")
window.resizable(False, False)

def delete_audio(videopath=None):
    if not videopath: return print("Video path is none!")
    threads = int(box.get())
    if (threads <= 0 or threads > __import__("os").cpu_count() or not threads):return messagebox.showerror("Ошибка","шизик?")
    if (box2.get() not in ["ultrafast", "superfast", "veryfast", "faster", "fast",
                            "medium", "slow", "slower", "veryslow", "placebo"]):return messagebox.showerror("Ошибка","шизик?")
    try:video = VideoFileClip(videopath)
    except OSError:return messagebox.showerror("Ошибка","Выбранный файл повреждён или недоступен.")
    video.audio = None
    video.write_videofile(filename='saved.mp4', fps=int(box1.get()), threads=threads, preset=box2.get())
    if (messagebox.askquestion("Рендер успешен!", "Открыть директорию?", icon="info") == "yes"):
        __import__("os").startfile(__import__("os").getcwd())

def main():
    fileName = easygui.fileopenbox()
    if fileName:
        if fileName.endswith(".mp4") or fileName.endswith(".flv") or fileName.endswith(".amv") or fileName.endswith(".wmv") or fileName.endswith(".avi"):
            delete_audio(fileName)
            return None


Button(text="Delete audio", command=main, bg="#3f966c", fg="white", font="Consolas 15 bold", width=17, height=1).pack(side=BOTTOM, pady=5)
Label(text="Threads: ", bg="#59566e", fg="white", font="Consolas 15 bold").place(x=4)
vals = []
for i in range(1, __import__("os").cpu_count()+1):
    vals.append(i)
box = ttk.Combobox(values=vals, height=15)
box.place(x=98, y=5)
box.current(0)

Label(text="FPS: ", bg="#59566e", fg="white", font="Consolas 15 bold").place(x=4, y=37)
box1 = ttk.Combobox(values=["29", "30", "59", "60", "120", "240", "480", "840"])
box1.place(x=53, y= 40)
box1.current(0)
# ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow, placebo
Label(text="Preset: ", bg="#59566e", fg="white", font="Consolas 15 bold").place(x=4, y=72)
box2 = ttk.Combobox(values=["ultrafast", "superfast", "veryfast", "faster", "fast",
                            "medium", "slow", "slower", "veryslow", "placebo"])
box2.place(x=85, y=77)
box2.current(5)

window.mainloop()
