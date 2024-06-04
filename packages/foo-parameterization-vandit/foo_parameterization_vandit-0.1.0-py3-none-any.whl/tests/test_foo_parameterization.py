import unittest
import math
from foo_parameterization.foo_parameterization import FooParameterization # type: ignore

class TestFooParameterization(unittest.TestCase):
    def test_calculate_volume(self):
        #test foo with positive given radiua
        radius = 3
        foo = FooParameterization(radius)
        expected_volume = (4/3) * math.pi * (radius ** 3)

    def test_negative_radius(self):
        #test foo with ngeative given radius and raises a value error 
        with self.assertRaises(ValueError):
            FooParameterization(-1)

    def test_zero_radius(self):
        #test foo with a zero radius and raises a value error 
        with self.assertRaises(ValueError):
            FooParameterization(0)

if __name__ == "__main__":
    unittest.main()
