import unittest

from hello_world import subtract


class TestHelloWorld(unittest.TestCase):

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(0, 0), 0)


if __name__ == "__main__":
    unittest.main()
# tests/test_hello_world.py
