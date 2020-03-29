import unittest
from LeaveManagement import LeaveManagement, PaidTimeOff, FlexTime, WorkFromHome


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


class TestFlexTime(unittest.TestCase):

    def test_display_id(self):
        test = FlexTime(4321, ("Gizmo", "Muzzy"), 0, 0)
        result = test.display_id()
        self.assertEqual(result, 4321,  'Should be 4321')

    def test_display_name(self):
        test = FlexTime(4321, ("Gizmo", "Muzzy"), 0, 0)
        result = test.display_name()
        self.assertEqual(result, 'Gizmo Muzzy', "Should be 'Gizmo Muzzy'")

    def test_display_hours(self):
        test = FlexTime(4321, ("Gizmo", "Muzzy"), 0, 0)
        result = test.display_hours()
        self.assertEqual(result, 0, "Should be 0")

    def test_add_flex(self):
        test = FlexTime(4321, ("Gizmo", "Muzzy"), 0, 0)
        test.add_flex(52)
        result = test.display_hours()
        self.assertEqual(result, 12, "Should be 12")


class TestWorkFromHome(unittest.TestCase):

    def test_display_id(self):
        test = WorkFromHome(1111, ("Mystery", "Person"), 16, 0)
        result = test.display_id()
        self.assertEqual(result, 1111,  'Should be 1111')

    def test_display_name(self):
        test = WorkFromHome(1111, ("Mystery", "Person"), 16, 0)
        result = test.display_name()
        self.assertEqual(result, 'Mystery Person',
                         "Should be 'Mystery Person'")

    def test_display_hours(self):
        test = WorkFromHome(1111, ("Mystery", "Person"), 16, 0)
        result = test.display_hours()
        self.assertEqual(result, 16, "Should be 16")

    def test_deduct_wfh(self):
        test = WorkFromHome(1111, ("Mystery", "Person"), 16, 0)
        test.deduct_wfh(8)
        result = test.display_hours()
        self.assertEqual(result, 8, "Should be 8")


if __name__ == '__main__':
    unittest.main()
