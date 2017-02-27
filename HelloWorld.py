import subprocess
import tkinter as tk
from tkinter import messagebox

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",command=root.destroy)
        self.quit.pack(side="bottom")
        self.showIp = tk.Button(self,text="SHOW IP INFO",fg="blue", command=self.show_alert)
        self.showIp.pack(side="left")

    def say_hi(self):
        print("hi there, everyone!")

    def show_ipInfo(self):
    	return subprocess.run("ifconfig")

    def show_alert(self):
       proc = proc = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE, shell=True)
       (out, err) = proc.communicate()
       messagebox.showinfo("INFO",out)

root = tk.Tk()
app = Application(master=root)
app.mainloop()
