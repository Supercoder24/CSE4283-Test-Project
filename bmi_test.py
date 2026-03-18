import pytest
from bmi import BMI

bmi = BMI()

# Weak Nx1 Testing, with N = 1
#   3 Boundaries, so 
#   Weak 1x1 = (1+1)*3 + 1 = 7 tests

# Boundary 1
# BMI = 18.5 Underweight
def test_under():
  out = bmi.main(4,8,80.5)
  # Use flooring to account for 0.1 error
  assert int(out[0]*10) == 184
  assert out[1] == 'Underweight'

# BMI = 18.6 Normal Weight
def test_normal_min():
  out = bmi.main(4,8,80.6)
  # Use flooring to account for 0.1 error
  assert int(out[0]*10) == 185
  assert out[1] == 'Normal Weight'

# Interior
# BMI = 22 Normal Weight
def test_normal_int():
  out = bmi.main(5,10,150)
  # Use flooring to account for 0.1 error
  assert int(out[0]*10) == 220
  assert out[1] == 'Normal Weight'

# Boundary 2
# BMI = 24.9 Normal Weight
def test_normal_max():
  out = bmi.main(6,8,222)
  # Use flooring to account for 0.1 error
  assert int(out[0]*10) == 249
  assert out[1] == 'Normal Weight'

# BMI = 25   Overweight
def test_over_min():
  out = bmi.main(6,8,223)
  # Use flooring to account for 0.1 error
  assert int(out[0]*10) == 250
  assert out[1] == 'Overweight'

# Boundary 3
# BMI = 29.9 Overweight
def test_over_max():
  out = bmi.main(6,0,215.5)
  # Use flooring to account for 0.1 error
  assert int(out[0]*10) == 299
  assert out[1] == 'Overweight'

# BMI = 30 Obese
def test_obese():
  out = bmi.main(6,0,216)
  # Use flooring to account for 0.1 error
  assert int(out[0]*10) == 300
  assert out[1] == 'Obese'