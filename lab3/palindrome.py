w1 = "Oxo"
w2 = "oxo"

def checkpal(string):
  inverse = string[::-1]
  if inverse == string:
    print("true")
  else:
    print("false")

checkpal(w1)
checkpal(w2)