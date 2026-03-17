# Assignment 2

# Body Mass Index Calculator

# Input height in feet and inches
# Input weight in pounds
# Return BMI value and category

class BMI:
  def __init__(self):
    self.desc = "Body Mass Index Calculator"

  # Run in CLI, with user inputs
  def run(self):
    print("Welcome to the Body Mass Index Calculator!")

    # Gather inputs
    try:
      print()
      print("Please input height")
      feet = int(input("Feet: "))
      inches = float(input("Inches: "))

      if feet < 0 or inches < 0 or (feet == 0 and inches == 0):
        print("Invalid height. Please try again.")
        return

      print()
      print("Please input weight")
      pounds = float(input("Pounds: "))
      if pounds < 0:
        print("Invalid weight. Please try again.")
        return
      
    except:
      print("Invalid input. Please try again.")
      return

    # Execute functionality
    output = self.main(feet, inches, pounds)

    # Print outputs
    print("Calculated BMI: " + str(output[0]))
    print("BMI Category:   " + output[1])


  # Convert height in feet and inches to meters
  def heightToMeters(self, feet, inches):
    return 0
  
  # Convert weight in pounds to kilograms
  def weightToKg(self, pounds):
    return 0
  
  # Calculate Body Mass Index based on height and weight
  def calcBMI(self, meters, kg):
    return 0
  
  # Get BMI category based on BMI
  def getCategory(self, bmi):
    return ''
  
  # Execute functionality
  def main(self, feet, inches, pounds):
    return (0, '')