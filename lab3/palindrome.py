import sys

def checkpal(string):
  inverse = string[::-1]
  if inverse == string:
    print("true")
  else:
    print("false")
    
checkpal(sys.argv[1])