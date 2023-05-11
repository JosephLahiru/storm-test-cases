import unittest

from scripts.Storm_Centre import Storm_Centre
from scripts.Hurricane import Hurricane
from scripts.Blizzard import Blizzard

class TestStorm_Centre(unittest.TestCase):

    def test_add_storm(self):
        storm_centre = Storm_Centre()
        hurricane = Hurricane("Hurricane", 74)
        self.assertEqual(storm_centre.add_storm(hurricane), True)
        self.assertEqual(len(storm_centre.storm_list), 1)

        blizzard = Blizzard("Blizzard", 35, 10)
        self.assertEqual(storm_centre.add_storm(blizzard), True)
        self.assertEqual(len(storm_centre.storm_list), 2)

        # Test for max storm limit
        with self.assertRaises(ValueError):
            storm_centre.add_storm(hurricane)

        # Test for duplicate storm name
        with self.assertRaises(ValueError):
            storm_centre.add_storm(hurricane)

    def test_remove_storm(self):
        storm_centre = Storm_Centre()
        hurricane = Hurricane("Hurricane", 74)
        storm_centre.add_storm(hurricane)

        self.assertEqual(storm_centre.remove_storm("Hurricane"), True)
        self.assertEqual(len(storm_centre.storm_list), 0)

        self.assertEqual(storm_centre.remove_storm("Hurricane"), False)

    def test_view_storm(self):
        storm_centre = Storm_Centre()
        hurricane = Hurricane("Hurricane", 74)
        storm_centre.add_storm(hurricane)

        blizzard = Blizzard("Blizzard", 35, 10)
        storm_centre.add_storm(blizzard)

        self.assertEqual(storm_centre.view_storm("Hurricane"), hurricane)
        self.assertEqual(storm_centre.view_storm("Blizzard"), blizzard)
        self.assertEqual(storm_centre.view_storm("Invalid Storm"), None)

    def test_update_storm(self):
        storm_centre = Storm_Centre()
        hurricane = Hurricane("Hurricane", 74)
        storm_centre.add_storm(hurricane)

        values = {"windspeed": 100}
        self.assertEqual(storm_centre.update_storm("Hurricane", values), True)
        self.assertEqual(hurricane.wind_speed, 100)

        # Test for invalid values
        with self.assertRaises(Exception):
            storm_centre.update_storm("Hurricane", "invalid")

    def test_already_exists(self):
        storm_centre = Storm_Centre()
        hurricane = Hurricane("Hurricane", 74)
        storm_centre.add_storm(hurricane)

        self.assertEqual(storm_centre.already_exists("Hurricane"), True)
        self.assertEqual(storm_centre.already_exists("Invalid Storm"), False)


if __name__ == "__main__":
    unittest.main()
