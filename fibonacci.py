import sys
def fibonacci(n): #generator function
   a, b, counter = 0, 1, 0
   while True:
      if (counter > n):
         return
      yield a
      a, b = b, a + b
      counter += 1

num = int(input("Digite um número:\n"))
f = fibonacci(num) #f is iterator object

while True:
   try:
      print (next(f), end="\n")
   except StopIteration:
      sys.exit()
