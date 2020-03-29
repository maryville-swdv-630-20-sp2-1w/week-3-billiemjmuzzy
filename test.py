import unittest
from LeaveManagement import LeaveManagement, PaidTimeOff


class TestLeaveManagement(unittest.TestCase):

    def test_display_id(self):
        test = LeaveManagement(1121, ("Billie", "Muzzy"), 10)
        result = test.display_id()
        self.assertEqual(result, 1121,  'Should be 1121')

    def test_display_name(self):
        test = LeaveManagement(1121, ("Billie", "Muzzy"), 10)
        result = test.display_name()
        self.assertEqual(result, 'Billie Muzzy', "Should be 'Billie Muzzy'")

    def test_display_hours(self):
        test = LeaveManagement(1121, ("Billie", "Muzzy"), 10)
        result = test.display_hours()
        self.assertEqual(result, 10, "Should be 10")


class TesPaidTimeOff(unittest.TestCase):

    def test_display_id(self):
        test = PaidTimeOff(1234, ("Atlas", "Muzzy"), 23, 0, 0)
        result = test.display_id()
        self.assertEqual(result, 1234, "Should be 0408")

    def test_display_name(self):
        test = PaidTimeOff(1234, ("Atlas", "Muzzy"), 23, 0, 0)
        result = test.display_name()
        self.assertEqual(result, 'Atlas Muzzy', "Should be 'Atlas Muzzy'")

    def test_display_hours(self):
        test = PaidTimeOff(1234, ("Atlas", "Muzzy"), 23, 0, 0)
        result = test.display_hours()
        self.assertEqual(result, 23, "Should be 23")

    def test_add_hours(self):
        test = PaidTimeOff(1234, ("Atlas", "Muzzy"), 23, 0, 0)
        test.add_hours(2)
        result = test.display_hours()
        self.assertEqual(result, 25, "Should be 25")

    def test_subtract_hours(self):
        test = PaidTimeOff(1234, ("Atlas", "Muzzy"), 23, 0, 0)
        test.subtract_hours(10)
        result = test.display_hours()
        self.assertEqual(result, 13, "Should be 13")

    def test_display_accrued(self):
        test = PaidTimeOff(1234, ("Atlas", "Muzzy"), 23, 0, 0)
        test.add_hours(10)
        test.subtract_hours(1)
        test.add_hours(10)
        result = test.display_accrued()
        self.assertEqual(result, 20, "Should be 20")

    def test_display_taken(self):
        test = PaidTimeOff(1234, ("Atlas", "Muzzy"), 23, 0, 0)
        test.add_hours(10)
        test.subtract_hours(1)
        test.subtract_hours(6)
        result = test.display_taken()
        self.assertEqual(result, 7, "Should be 7")


if __name__ == '__main__':
    unittest.main()
