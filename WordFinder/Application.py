# -*- coding:utf-8 -*-
import tkinter as tk
import os
from tkinter.filedialog import askopenfilename
from tkinter import StringVar
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
	def __init__(self,master=None):
		super().__init__(master)
		self.word = tk.StringVar()
		self.directory_path = tk.StringVar()
		self.lb_directory_path = tk.Label(self)
		self.pack()
		self.create_widgets()

	# create app compoents
	def create_widgets(self):
		# Search Folder Button
		self.lb_word    = tk.Label(self, text="Palavra que quer pesquisar: ").grid(row=0)
		self.input_word = tk.Entry(self,textvariable=self.word).grid(row=0, column=1)
		self.btn_directory_path = tk.Button(
			self,text="Procupar Pasta",
			command=self.get_directory,
		).grid(row=1)
		self.lb_directory_path.grid(row=1,column=1)

		self.btn_search_files = tk.Button(
			self,text="Pesquisar",
			command=self.search_files,
		).grid(row=2)

	#find files
	def find_files(self,word,file_path):
		try:
			text = textract.process(file_path)
			textEncoded = text.decode('utf-8')
			hasTheWord = textEncoded.find(word)
			if(hasTheWord != -1) :
				print(file_path)
				return file_path
		except:
			pass

	#list all the directories in given path
	def list_files(self,startpath,word):
		files = []
		for root, dirs, files in os.walk(startpath):
			level = root.replace(startpath, '').count(os.sep)
			indent = ' ' * 4 * (level)
			dir = '{}{}/'.format(indent, os.path.basename(root))
			# print(dir)
			subindent = ' ' * 4 * (level + 1)
			for f in files:
				files = self.find_files(word,root+'/'+'{}{}'.format(subindent, f).strip())
				# print('{}{}'.format(subindent, f))
		return files

	def search_files(self):
		startpath = str(self.directory_path.get())
		word = str(self.word.get())
		found_files = self.list_files(startpath,word)
		# print(str(found_files))

	# search and select diretory
	def get_directory(self):
		dir_opt = {}
		dir_opt['initialdir'] = os.environ["HOME"] + '\\'
		dir_opt['mustexist'] = False
		dir_opt['title'] = 'Please select directory'
		self.directory_path.set(askdirectory(**dir_opt))
		self.lb_directory_path['text'] = self.directory_path.get()
		print(self.word.get())
		print(self.directory_path.get())


root = tk.Tk()
root.title("Word Finder")
root.geometry("650x400")
app = Application(master=root)
app.mainloop()
