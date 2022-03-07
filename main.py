def bad():
  #ignore this all it was wrong
  x="    "
  num1=5
  num2=1
  y = "*****"
  for count in range(1,6):
    for i in range(1,6):
      print(x[:num1] + y[:num2])
      num1-=1
      num2+=1

#the top
def top():
  space=5
  #spaces printed
  for i in range(1,6):
    #to print the spaces
    for k in range(1,space):
      print(" ", end="")
      #to print the stars
    for j in range(1,i+1):
      print("*", end=" ")
    print()
    space-=1 #decreases spaces to even out stars

#the bottom
def bottom():
  space=2
  #spaces printed
  for i in range(6,1,-1):
    #prints the spaces
    for k in range(1,space):
      print(" ", end="")
      #prints the stars
    for j in range(1,i-1):
      print("*", end=" ")
    print()
    space+=1 #increase spaces to even out stars

#run
top()
bottom()