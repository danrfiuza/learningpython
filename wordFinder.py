# install pip3 and then run pip3 install textract
from sys import exit
import textract
word = ''
word = input('TYPE A WORD YOU WANNA SEARCH IN FILES:')
text = textract.process('relatorio.pdf')
textEncoded = text.decode('utf-8')
hasTheWord = textEncoded.find(word)
if(hasTheWord != -1) :
	print('THIS DOCUMENT HAS THE WORD THA YOU\'RE LOOKING FOR! YAY!')
	exit(0)

print('THE WORD YOU\'RE SEARCHING WAS NOT FOUND. GO AWAY')


def list_files(startpath):
	for root, dirs, files in os.walk(startpath):
		level = root.replace(startpath, '').count(os.sep)
		indent = ' ' * 4 * (level)
		print('{}{}/'.format(indent, os.path.basename(root)))
		subindent = ' ' * 4 * (level + 1)
		for f in files:
			print('{}{}'.format(subindent, f))

startpath = '/home/danielfiuza/projetos/learningpython'
list_files(startpath)
print(os.walk(startpath))
