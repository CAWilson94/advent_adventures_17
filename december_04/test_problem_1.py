from unittest import TestCase
from december_04 import problem_1 as p1
from december_04 import input_file_creator as ifc


class TestProblem1(TestCase):
    def test_problem_1(self):
        puzzle_input = ifc.input_from_file("passphrases.txt")
        puzzle_list = p1.split_strings_to_list(puzzle_input)
        fake_input = [["aa", "bb", "cc", "dd", "aa"], ["aa", "bb", "bb", "dd", "aa"], ["aa" "bb", "cc", "dd", "aaa"]]
        self.assertEquals(1, p1.problem_1(fake_input))
        self.assertEquals(451, p1.problem_1(puzzle_list))
