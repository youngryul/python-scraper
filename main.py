first = 0
second = 0
operation = ''
result = 0

def calc():
  print("Choose a number : ")
  first = int(input())
  
  print("Choose another one : ")
  second = int(input())
  
  print('''Choose an operation
              Options are: +, -, * or /.
              Write 'exit' to finish.''')
  operation = input()

  return first, second, operation


while True:
  first, second, operation = calc()

  if operation == 'exit':
    break
  
  if(operation == '+'):
    result = first + second
  elif(operation == '-'):
    result = first - second
  elif(operation == '*'):
    result = first * second
  elif(operation == '/'):
    result = first / second
    
  print("Result : ", result)
