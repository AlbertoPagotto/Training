"Calculator"

def calculator():
  def add(n1,n2):
    return n1+n2
  
  def subtract(n1,n2):
    return n1-n2
  
  def multiply(n1,n2):
    return n1*n2
  
  def divide(n1,n2):
    return n1/n2
  
  op_dict= {
    "+": "Add",
    "-": "Subtract",
    "*": "Multiply",
    "/": "Divide"
  }
  
  num1=float(input("What's the first number? "))
  num2=float(input("What's the second number? "))
  for key in op_dict:
    print(key)
  
  function=input("Pick an operation from the line above: ")
  
  if function=="+":
    answer=add(num1,num2)
  elif function=="-":
    answer=subtract(num1,num2)
  elif function=="*":
    answer=multiply(num1,num2)
  elif function=="/":
    answer=divide(num1,num2)
  else:
    print("ERROR: wrong input")
  
  print(f"{num1} {function} {num2} = {answer}")

  should_continue=input("Should I continue (y/n)? ")
  if should_continue=="y":
    calculator()

calculator()