from unittest import TestCase
from december_01 import problem_two as p2, file_input as fi


class TestNonHumanCaptcha2(TestCase):

    def test_non_human_captcha_2(self):
        test_example_one = [1, 2, 1, 2]
        test_example_two = [1, 2, 3, 4, 2, 5]
        test_example_three = [1, 2, 3, 1, 2, 3]
        test_example_four = [1, 2, 1, 3, 1, 4, 1, 5]
        text_file_input = fi.file_input_to_int_list("input.txt")
        result_1 = p2.non_human_captcha_2(test_example_one)
        result_2 = p2.non_human_captcha_2(test_example_two)
        result_3 = p2.non_human_captcha_2(test_example_three)
        result_4 = p2.non_human_captcha_2(test_example_four)
        result_file = p2.non_human_captcha_2(text_file_input)
        self.assertEqual(6, result_1)
        self.assertEqual(4, result_2)
        self.assertEqual(12, result_3)
        self.assertEqual(4, result_4)
        self.assertEqual(1420, result_file)

