import unittest
class A:
   def __init__(self,one,two):
     self.one = one
     self.two = two
class TA(unittest.TestCase):
   def test_a(self):
     c = A(1,2)
     self.assertEqual(c.one,1)
     self.assertEqual(c.two,2)
c=A(1,2)
c
# val: <__main__.A object at 0x7f62bae9d890>
if __name__ == "__main__":
    unittest.main()
