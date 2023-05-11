# This script defines the Hurricane class. A hurricane is a large, rotating storm that forms over warm waters in the tropics. 
# Hurricanes are characterized by strong winds, heavy rain, and storm surges. 
# The Hurricane class inherits from the Storm class, which defines the basic properties of a storm, such as its name and wind speed. 
# The Hurricane class adds additional properties, such as the hurricane's intensity.

# The Hurricane class has two methods: calculate_classification() and get_advice(). 
# The calculate_classification() method calculates the hurricane's classification, such as "Category one", "Category two", or "F5". The get_advice() method returns advice for how to stay safe during a hurricane.

import unittest

from scripts.Hurricane import Hurricane

class TestHurricane(unittest.TestCase):

    def test_calculate_classification(self):
        hurricane = Hurricane("Hurricane", 74)
        self.assertEqual(hurricane.calculate_classification(), "Category two")

    def test_get_advice(self):
        hurricane = Hurricane("Hurricane", 74)
        self.assertEqual(hurricane.get_advice(), "Coastal regions are encouraged to evacuate")

if __name__ == "__main__":
    unittest.main()
