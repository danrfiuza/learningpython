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
