from unittest import TestCase
from december_1 import problem_one as p1, file_input as fi


class TestNonHumanCaptcha(TestCase):
    def test_non_human_captcha(self):
        test_example_one = [1, 1, 2, 2]
        test_example_two = [1, 1, 1, 1]
        test_example_three = [1, 2, 3, 4]
        test_example_four = [9, 1, 2, 1, 2, 1, 2, 9]
        text_file_input = fi.file_input_to_int_list("input.txt")
        result_1 = p1.non_human_captcha(test_example_one)
        result_2 = p1.non_human_captcha(test_example_two)
        result_3 = p1.non_human_captcha(test_example_three)
        result_4 = p1.non_human_captcha(test_example_four)
        result_file = p1.non_human_captcha(text_file_input)
        self.assertEqual(3, result_1)
        self.assertEqual(4, result_2)
        self.assertEqual(0, result_3)
        self.assertEqual(9, result_4)
        self.assertEqual(1119, result_file)
