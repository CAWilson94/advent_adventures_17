from unittest import TestCase
from december_03 import problem_1 as p1


class TestGetNumMoves(TestCase):
    def test_get_num_moves(self):
        self.assertEqual(0, p1.get_num_moves(1))
        self.assertEqual(3, p1.get_num_moves(12))
        self.assertEqual(31, p1.get_num_moves(1024))
        self.assertEqual(475, p1.get_num_moves(277678))

