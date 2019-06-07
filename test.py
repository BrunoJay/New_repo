def t():
	return("Python welcomes software engineering recess term 2019")

print (t())

fruits = ["mango", "banana", "cherry"]

for fruit in fruits:
	print(fruit[2:])



def max1(x, y): 
  #Takes comparable values x and y as arguments.
  #Returns the larger of the two, implemented with if-else. 
  if x > y:
     return x
  else:
     return y


def max2(x, y):
  #Takes comparable values x and y as arguments.
  #Returns the larger of the two, implemented with if (no else).
  if x > y:
     return x
  return y


a = 6
b = 2
print("Max1:", max1(5, 34))
print("Max2:", max2(a, b))