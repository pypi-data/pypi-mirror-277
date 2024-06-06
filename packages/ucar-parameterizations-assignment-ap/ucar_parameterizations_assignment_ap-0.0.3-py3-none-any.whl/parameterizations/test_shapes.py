import unittest
import shapes

class TestSphereMethods(unittest.TestCase):
  
  def test_calc_perimeter(self):
    # no parameters
    sphere = shapes.Sphere()
    self.assertEqual(sphere.calc_perimeter(), 0)
    # given radius
    self.assertEqual(round(sphere.calc_perimeter(radius=5),2), 31.42)
    # shape's radius field
    sphere.radius = 7
    self.assertEqual(sphere.radius, 7)
    self.assertEqual(round(sphere.calc_perimeter(),2), 43.98)
    
  def test_calc_volume(self):
    # no parameters
    sphere = shapes.Sphere()
    self.assertEqual(sphere.calc_volume(), 0)
    # given radius
    self.assertEqual(round(sphere.calc_volume(radius=5), 1), 523.6)
    # shape's radius field
    sphere.radius = 7
    self.assertEqual(round(sphere.calc_volume(),2), 1436.76)
    
if __name__ == '__main__':
  unittest.main()