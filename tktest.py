import tkinter # note that module name has changed from Tkinter in Python 2 to tkinter in Python
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory

import os
root = tkinter.Tk()
# search for files
# ftypes = [('all files', '.*')]
# ttl  = "Title"
# dir1 = '/home'
# root.fileName = askopenfilename(filetypes = ftypes, initialdir = dir1, title = ttl)
# print(root.fileName)

# search in directory
dir_opt = {}
dir_opt['initialdir'] = os.environ["HOME"] + '\\'
dir_opt['mustexist'] = False
dir_opt['title'] = 'Please select directory'
root.folderName = askdirectory(**dir_opt)
print(root.folderName)

