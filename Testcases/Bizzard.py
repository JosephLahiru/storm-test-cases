# This script defines the Blizzard class. 
# A blizzard is a severe winter storm characterized by strong winds, low visibility, and heavy snow. 
# The Blizzard class inherits from the Storm class, which defines the basic properties of a storm, such as its name and wind speed. 
# The Blizzard class adds additional properties, such as the blizzard's temperature.

# The Blizzard class has two methods: calculate_classification() and get_advice(). 
# The calculate_classification() method calculates the blizzard's classification, such as "Blizzard", "Severe Blizzard", or "Snow Storm". 
# The get_advice() method returns advice for how to stay safe during a blizzard.

import unittest

from scripts.Blizzard import Blizzard

class TestBlizzard(unittest.TestCase):

    def test_calculate_classification(self):
        blizzard = Blizzard("Blizzard", 35, -10)
        self.assertEqual(blizzard.calculate_classification(), "Blizzard")

        blizzard = Blizzard("Blizzard", 45, -12)
        self.assertEqual(blizzard.calculate_classification(), "Severe Blizzard")

        blizzard = Blizzard("Blizzard", 34, -10)
        self.assertEqual(blizzard.calculate_classification(), "Snow Storm")

    def test_get_advice(self):
        blizzard = Blizzard("Blizzard", 35, -10)
        self.assertEqual(blizzard.get_advice(), "Keep warm, Do not travel unless absolutely essential.")

        blizzard = Blizzard("Blizzard", 45, -12)
        self.assertEqual(blizzard.get_advice(), "Keep warm, avoid all travel.")

        blizzard = Blizzard("Blizzard", 34, -10)
        self.assertEqual(blizzard.get_advice(), "Take care and avoid travel if possible.")

if __name__ == "__main__":
    unittest.main()
