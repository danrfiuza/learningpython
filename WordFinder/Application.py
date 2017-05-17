# -*- coding:utf-8 -*-
import tkinter as tk
import os
import webbrowser
from tkinter.filedialog import askopenfilename
from tkinter import StringVar
from tkinter import Listbox
from tkinter.filedialog import askdirectory
import textract
from sys import exit


# search for files
# ftypes = [('all files', '.*')]
# ttl  = "Title"
# dir1 = '/home'
# root.fileName = askopenfilename(filetypes = ftypes, initialdir = dir1, title = ttl)
# print(root.fileName)

# search in directory
# dir_opt = {}
# dir_opt['initialdir'] = os.environ["HOME"] + '\\'
# dir_opt['mustexist'] = False
# dir_opt['title'] = 'Please select directory'
# root.folderName = askdirectory(**dir_opt)
# print(root.folderName)

class Application(tk.Frame):
	# constructor
	def __init__(self, master=None):
		super().__init__(master)
		self.word = tk.StringVar()
		self.directory_path = tk.StringVar()
		self.lb_directory_path = tk.Label(self)
		self.pack()
		self.create_widgets()

	# create app compoents
	def create_widgets(self):
		# Search Folder Button
		self.lb_word = tk.Label(self, text="Informe a palavra que deseja pesquisar: ")
		self.lb_word.grid(row=0, column=0,padx=0,columnspan=1,ipady=10,sticky='W')

		self.input_word = tk.Entry(self, textvariable=self.word)
		self.input_word.grid(row=1, column=0,sticky='W',ipady=10,ipadx=250)

		self.btn_directory_path = tk.Button(self, text="Informe o Diretório",command=self.get_directory,)
		self.btn_directory_path.grid(row=2,column=0,sticky='W')
		self.lb_directory_path.grid(row=2, column=0,sticky='E')

		self.btn_search_files = tk.Button(self, text="Pesquisar",command=self.search_files,)
		self.btn_search_files.grid(row=3,ipady=10,ipadx=60,pady=20)

		self.lb_word = tk.Label(self, text="Arquivos Encontrados: ")
		self.lb_word.grid(row=4,ipady=10)

		self.scroll_bar = tk.Scrollbar(self)
		self.scroll_bar.grid(row=5,column=0)

		self.list_box   = tk.Listbox(self,selectmode='SINGLE',width=80, height=20)
		self.list_box.grid(row=5,column=0,ipady=20)
		# self.list_box.bind("<Double-Button-1>", self.onDouble)
		self.list_box.bind("<Double-Button-1>",self.onDouble)
		# attach listbox to scrollbar
		self.list_box.config(yscrollcommand=self.scroll_bar.set)
		self.scroll_bar.config(command=self.list_box.yview)

	# find files
	def find_files(self, word, file_path):
		try:
			text = textract.process(file_path)
			textEncoded = text.decode('utf-8')
			hasTheWord = textEncoded.find(word)
			if (hasTheWord != -1):
				self.list_box.insert('end', file_path)
				print(file_path)
				# return file_path
		except:
			pass

	# list all the directories in given path
	def list_files(self, startpath, word):
		files_array = []
		for root, dirs, files in os.walk(startpath):
			level = root.replace(startpath, '').count(os.sep)
			indent = ' ' * 4 * (level)
			dir = '{}{}/'.format(indent, os.path.basename(root))
			# print(dir)
			subindent = ' ' * 4 * (level + 1)
			for f in files:
				self.find_files(word, root + '/' + '{}{}'.format(subindent, f).strip())
			# print('{}{}'.format(subindent, f))
		return files_array

	def search_files(self):
		startpath = str(self.directory_path.get())
		word = str(self.word.get())
		self.list_box.delete(0, 'end')
		self.list_files(startpath, word)
		# for file in found_files:
		#     self.list_box.insert('end', file)
		# print(str(found_files))

	#function to select the file path on list box
	def onDouble(self, event):
		widget = event.widget
		selection = widget.curselection()
		filepath = widget.get(selection[0])
		webbrowser.open(filepath)
		# os.system("open "+value)
		# subprocess.call(('open', filepath))
		os.startfile(filepath)
		print(filepath)

	# search and select diretory
	def get_directory(self):
		dir_opt = {}
		dir_opt['initialdir'] = os.path.abspath('..')
		dir_opt['mustexist'] = False
		dir_opt['title'] = 'Please select directory'
		self.directory_path.set(askdirectory(**dir_opt))
		self.lb_directory_path['text'] = self.directory_path.get()
		print(self.word.get())
		print(self.directory_path.get())


root = tk.Tk()
root.title("Word Finder")
root.geometry("800x600")
app = Application(master=root)
app.mainloop()
