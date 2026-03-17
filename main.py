# Imports
from bmi import BMI

# Global function selector

print("Welcome to my CSE4283 project!")
print()

while True:
  print("Please select a function from the following list:")

  functions = [
    BMI()
  ]

  ind = 'a'

  for func in functions:
    print('  ' + ind + ') ' + func.desc)
    ind = chr(ord(ind) + 1)

  print('  x) Exit the program')

  selection = input("Pick a choice: ")

  if selection == 'x':
    exit(0)
  else:
    print()
    try:
      index = ord(selection) - 97
      if (index >= 0 and index < len(functions)):
        functions[index].run()
      else:
        print("Choice unavailable. Please try again.")
    except:
      print("Invalid choice. Please try again.")
  print()