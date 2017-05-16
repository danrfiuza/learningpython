import os
import textract
from sys import exit

def findTheWord(word,file):
	# word = input('TYPE A WORD YOU WANNA SEARCH IN FILES:')
	try:
		text = textract.process(file)
		textEncoded = text.decode('utf-8')
		hasTheWord = textEncoded.find(word)
		if(hasTheWord != -1) :
			print('WORD FOUND IN FILE:\n'+file)
	except:
		pass


def list_files(startpath,word):
	for root, dirs, files in os.walk(startpath):
		level = root.replace(startpath, '').count(os.sep)
		indent = ' ' * 4 * (level)
		dir = '{}{}/'.format(indent, os.path.basename(root))
		# print(dir)
		subindent = ' ' * 4 * (level + 1)
		for f in files:
			findTheWord(word,root+'/'+'{}{}'.format(subindent, f).strip())
			# print('{}{}'.format(subindent, f))

word = input('TYPE A WORD YOU WANNA SEARCH IN FILES:')
startpath = input('NOW TYPE THE PATH FROM IN WHICH DIRECTORY YOU WANNA SEEK:\n')
list_files(startpath,word)
# /home/danielfiuza/projetos/learningpython
