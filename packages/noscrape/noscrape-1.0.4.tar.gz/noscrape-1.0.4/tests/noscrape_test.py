import unittest

from noscrape import Noscrape


class TestNoscrape(unittest.TestCase):
    def test_noscrape(self):
        n = Noscrape("../example/example.ttf")

        xy = n.obfuscate("test")
        self.assertNotEqual(xy, "test")

        xyz = n.render()
        self.assertNotEqual(xyz, "test")


if __name__ == '__main__':
    unittest.main()
