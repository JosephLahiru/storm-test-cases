# This script defines the Storm_Centre class.
# A storm centre is a facility that monitors and tracks storms. 
# The Storm_Centre class has four methods: add_storm(), remove_storm(), view_storm(), and update_storm(). 
# The add_storm() method adds a storm to the storm centre's list of storms. The remove_storm() method removes a storm from the storm centre's list of storms. The view_storm() method returns the storm with the specified name. 
# The update_storm() method updates the properties of a storm.

import unittest

from scripts.Storm_Centre import Storm_Centre

class TestStorm_Centre(unittest.TestCase):

    def test_add_storm(self):
        storm_centre = Storm_Centre()
        self.assertTrue(storm_centre.add_storm(Hurricane("Hurricane", 74)))
        self.assertTrue(storm_centre.add_storm(Blizzard("Blizzard", 35, -10)))
        self.assertFalse(storm_centre.add_storm(Hurricane("Hurricane", 74)))
        self.assertFalse(storm_centre.add_storm(Blizzard("Blizzard", 35, -10)))

    def test_remove_storm(self):
        storm_centre = Storm_Centre()
        storm_centre.add_storm(Hurricane("Hurricane", 74))
        self.assertTrue(storm_centre.remove_storm("Hurricane"))
        self.assertFalse(storm_centre.remove_storm("Hurricane"))

    def test_view_storm(self):
        storm_centre = Storm_Centre()
        storm_centre.add_storm(Hurricane("Hurricane", 74))
        self.assertEqual(storm_centre.view_storm("Hurricane"), Hurricane("Hurricane", 7
