# Test script for testing various calculator functions

import SimpleCalculator as calc_func

class CalcTest:
  def __init__(self):
    self.status = None
    
  def test_add(self):
    result = calc_func.add(5, 3)
    assert result == 8, "Add test failed!"
    
  def test_subtract(self):
    result = calc_func.subtract(5, 3)
    assert result == 2, "Subtract test failed!"
    
  def test_multiply(self):
    result = calc_func.multiply(5, 3)
    assert result == 15, "Multiply test failed!"
  
  def test_divide(self):
    result = calc_func.divide(6, 3)
    assert result == 2, "Divide test failed!"
    
if __name__ == "__main__":
  ct = CalcTest()
  ct.test_add()
  ct.test_subtract()
  ct.test_multiply()
  ct.test_divide()
