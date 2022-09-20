import os.path
import unittest

from zdenek import CodingAssignment


class TestCodingAssignment(unittest.TestCase):
    def test_init(self):
        coding_assignment = CodingAssignment()
        self.assertTrue(coding_assignment._data == None)
        self.assertTrue(coding_assignment._error_data == None)
        self.assertTrue(coding_assignment._report == None)

    def test_load_data(self):
        coding_assignment = CodingAssignment()
        coding_assignment.load_data("good_input.csv")
        self.assertTrue(type(coding_assignment._data) == list)

    def test_load_data_invalid_input_missing(self):
        coding_assignment = CodingAssignment()
        with self.assertRaises(ValueError):
            coding_assignment.load_data("potato")

    def test_load_data_invalid_input_directory(self):
        coding_assignment = CodingAssignment()
        with self.assertRaises(ValueError):
            coding_assignment.load_data("..")

    def test_generate_report(self):
        coding_assignment = CodingAssignment()
        coding_assignment._data = [["2022-05-03 12:02:20", "10101", "Natalie May", "24.91"]]
        coding_assignment.generate_report()
        self.assertAlmostEqual(24.91, coding_assignment._report["10101"]["2022-05"])

    def test_save_report(self):
        coding_assignment = CodingAssignment()
        coding_assignment.load_data("good_input.csv")
        coding_assignment.generate_report()
        coding_assignment.save_report("output.csv")
        self.assertTrue(os.path.isfile("output.csv"))

    def test_save_report_invalid(self):
        coding_assignment = CodingAssignment()
        coding_assignment.load_data("good_input.csv")
        coding_assignment.generate_report()
        with self.assertRaises(FileNotFoundError):
            coding_assignment.save_report("")


if __name__ == "__main__":
    unittest.main()
