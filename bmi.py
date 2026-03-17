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
    print()
    print("Calculated BMI: " + str(output[0]))
    print("BMI Category:   " + output[1])


  # Convert height in feet and inches to meters
  def heightToMeters(self, feet, inches):
    return ((feet * 12) + inches) * 0.025
  
  # Convert weight in pounds to kilograms
  def weightToKg(self, pounds):
    return pounds * 0.45
  
  # Calculate Body Mass Index based on height and weight
  def calcBMI(self, meters, kg):
    return kg / (meters * meters)
  
  # Get BMI category based on BMI
  def getCategory(self, bmi):
    if bmi < 18.5:
      return 'Underweight'
    elif bmi <= 24.9:
      return 'Normal Weight'
    elif bmi <= 29.9:
      return 'Overweight'
    else:
      return 'Obese'
  
  # Execute functionality
  def main(self, feet, inches, pounds):
    height = self.heightToMeters(feet, inches)
    weight = self.weightToKg(pounds)
    bmi = self.calcBMI(height, weight)
    return (round(bmi, 1), self.getCategory(bmi))