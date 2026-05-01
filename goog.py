from Helpers.helpings import *



'''13.1 Derived classes
A class will commonly share attributes with another class, but with some additions or variations. Ex: A store inventory system might use a class called Item, having name and quantity attributes. But for fruits and vegetables, a class Produce might have the attributes name, quantity, and expiration date. Note that Produce is really an Item with an additional feature, so ideally a program could define the Produce class as being the same as the Item class but with the addition of an expiration date attribute.

Such similarity among classes is supported by indicating that a class is derived from another class, as shown below.

Figure 13.1.1: A derived class example: Class Produce is derived from class Items.
class Item:
    def __init__(self):
        self.name = ""
        self.quantity = 0

    def set_name(self, nm):
        self.name = nm

    def set_quantity(self, qnty):
        self.quantity = qnty

    def display(self):
        print(self.name, self.quantity)


class Produce(Item):  # Derived from Item
    def __init__(self):
        Item.__init__(self)  # Call base class constructor
        self.expiration = ""

    def set_expiration(self, expir):
        self.expiration = expir

    def get_expiration(self):
        return self.expiration

item1 = Item()
item1.set_name("Smith Cereal")
item1.set_quantity(9)
item1.display()

item2 = Produce()
item2.set_name("Apples")
item2.set_quantity(40)
item2.set_expiration("May 5, 2012")
item2.display()
print(f"  (Expires:({item2.get_expiration()}))")
Smith Cereal 9
Apples 40
  (Expires:(May 5, 2012))
'''

class Item:
  def __init__(self):
      self.name = ""
      self.quantity = 0

  def set_name(self, nm):
      self.name = nm

  def set_quantity(self, qnty):
      self.quantity = qnty

  def display(self):
      print(self.name, self.quantity)
      # out: Smith Cereal 9
      # out: Apples 40


class Produce(Item):  # Derived from Item
  def __init__(self):
      Item.__init__(self)  # Call base class constructor
      # val: None
      self.expiration = ""

  def set_expiration(self, expir):
      self.expiration = expir

  def get_expiration(self):
      return self.expiration

item1 = Item()
item1.set_name("Smith Cereal")
# val: None
item1.set_quantity(9)
# val: None
item1.display()
# val: None

item2 = Produce()
item2.set_name("Apples")
# val: None
item2.set_quantity(40)
# val: None
item2.set_expiration("May 5, 2012")
# val: None
item2.display()
# val: None
print(f"  (Expires:({item2.get_expiration()}))")
# out:   (Expires:(May 5, 2012))





INFO()
# out: /home/runner/workspace
# out: Fri May  1 12:21:06 AM UTC 2026
# out: ./.gitignore
# out: ./uv.lock
# out: ./pyproject.toml
# out: ./.upm/store.json1205111821
# out: ./.upm/store.json
# out: ./.pythonlibs/CACHEDIR.TAG
# out: ./.pythonlibs/.gitignore
# out: ./.pythonlibs/pyvenv.cfg
# out: ./.replit
# out: ./.git/description
# out: ./.git/FETCH_HEAD
# out: ./.git/COMMIT_EDITMSG
# out: ./.git/config
# out: ./.git/HEAD
# out: ./.git/ORIG_HEAD
# out: ./.git/index
# out: ./__pycache__/inline_output.cpython-311.pyc
# out: ./__pycache__/inline_output_v2.cpython-311.pyc
# out: ./__pycache__/main.cpython-311.pyc
# out: ./__pycache__/inline_output_v4.cpython-311.pyc
# out: ./__pycache__/inline_output_v3.cpython-311.pyc
# out: ./old/goog (copy).py
# out: ./old/goog (copy)2.py
# out: ./old/goog (copy)3.py
# out: ./old/example.txt
# out: ./old/greeting.txt
# out: ./old/log.txt
# out: ./old/MEEEEOWWWWWW.txt
# out: ./old/names.txt
# out: ./old/notes.txt
# out: ./old/sample.txt
# out: ./old/score.txt
# out: ./old/goog (copy)4.py
# out: ./old/real.txt
# out: ./old/inline_output.py
# out: ./old/goog (copy)5.py
# out: ./old/goog (copy)6.py
# out: ./old/inline_output_v2.py
# out: ./old/goog (copy)8.py
# out: ./old/goog (copy)9.py
# out: ./old/goog (copy)10.py
# out: ./old/goog (copy)7.py
# out: ./old/goog (copy)11.py
# out: ./old/goog (copy)12.py
# out: ./old/goog (copy)13.py
# out: ./old/goog (copy)14.py
# out: ./old/goog (copy)15.py
# out: ./cs2520_lec13_exceptions_exercises.md
# out: ./cs2520_lec13_exercises (2).md
# out: ./data/real.txt
# out: ./data/real.py
# out: ./data/module_a.py
# out: ./data/__init__.py
# out: ./data/module_b.py
# out: ./data/something.py
# out: ./data/Square.py
# out: ./data/generated-icon.png
# out: ./data/Figure13_1_1.py
# out: ./Helpers/helpings.py
# out: ./inline_output_v4.py
# out: ./goog (copy).py
# out: ./goog.py
# out: ./inline_output_v3.py
# out: ./main.py
