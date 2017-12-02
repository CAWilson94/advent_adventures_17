from unittest import TestCase
from december_02 import input_file_creator as ifc, problem_1 as p1


class TestCheckSum1(TestCase):
    def test_check_sum_1(self):
        input_one = ifc.input_from_file("test_input.csv")
        input_two = ifc.input_from_file("input.csv")
        result_one = p1.check_sum_1(input_one)
        result_two = p1.check_sum_1(input_two)
        self.assertTrue(18, result_one)
        self.assertTrue(36174, result_two)


