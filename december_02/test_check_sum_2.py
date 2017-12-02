from unittest import TestCase
from december_02 import input_file_creator as ifc, problem_2 as p2


class TestCheckSum2(TestCase):
    def test_check_sum_2(self):
        input_one = ifc.input_from_file("input.csv")
        input_two = ifc.input_from_file("input_2_test.csv")
        result_one = p2.check_sum_2(input_one)
        result_two = p2.check_sum_2(input_two)
        self.assertTrue(244, result_one)
        self.assertTrue(9, result_two)
