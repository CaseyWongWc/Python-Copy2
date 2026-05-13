# save: c13_3.py
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


class Produce(Item):  # Derived from Item
   def __init__(self):
       Item.__init__(self)  # Call base class constructor
       self.expiration = ""

   def set_expiration(self, expir):
       self.expiration = expir

   def get_expiration(self):
       return self.expiration

   def display(self):
       print(self.name, self.quantity, end=" ")
       print(f"  (Expires: {self.expiration})")

# out: Apples 40 
# out:  0 

item1 = Item()
# out:   (Expires: May 5, 2012)
# out:   (Expires: )
item1.set_name("Smith Cereal")
item1.set_quantity(9)
item1.display()  # Will call Item's display()

item2 = Produce()
item2.set_name("Apples")
item2.set_quantity(40)
# val: None
item2.set_expiration("May 5, 2012")

'''3)
Provide a statement within the display() method of the Produce class to call the display() method of Produce's base class.'''
item2.display()  # Will call Produce's display()
'''4)
If Produce did NOT have its own display() method defined, the display method of which class would be called in the following code? Type "ERROR" if appropriate.'''
p = Produce()
p.display()
