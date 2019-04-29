import unittest

from Qs.graphs import graph_medium

class TestGraphsMedium(unittest.TestCase):
    def test_keys_and_room(self):
        graph = [[1], [2], [3], []]
        #expected = graph_medium.keys_and_room(graph)
        expected = graph_medium.keys_and_room_better_storage(graph)
        self.assertTrue(expected)

    def test_keys_and_room_false(self):
        graph = [[1,3], [3,0,1], [2], [0]]
        #expected = graph_medium.keys_and_room(graph)
        expected = graph_medium.keys_and_room_better_storage(graph)
        self.assertFalse(expected)