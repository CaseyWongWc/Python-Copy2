from Helpers.helpings import *
import unittest

class Google:
    def __init__(self):
        self.knowledge =
class TestGoogle(unittest.TestCase):
    def test_google(self):
        self.assertEqual(google("What is the capital of France?"), "The capital of France is Paris.")
        self.assertEqual(google("Who is the president of the United States?"), "The president of the United States is Joe Biden.")
        self.assertEqual(google("What is the largest mammal?"), "The largest mammal is the blue whale.")
        self.assertEqual(google("What is the square root of 16?"), "The square root of 16 is 4.")
        self.assertEqual(google("What is the chemical symbol for water?"), "The chemical symbol for water is H2O.")

if __name__ == "__main__":
    unittest.main()
