# fig: 13.1.1  # auto-save to _zybooks/C_13/Figure_13_1_1.py
from Helpers.helpings import *

# 13.1.1: Derived classes.
'''challenge activity
13.1.2: Defining a derived class.
712910.5105864.qx3zqy7

Jump to level 1
Complete the definition of class Milkshake so that Milkshake is derived from the base class DrinkOrder.

Click here for example
Ex: If the input is:
Tia
Lynn
then the output is:
class DrinkOrder:
  def __init__(self):
      self.first_name = 0
      self.last_name = 0

  def set_first_name(self, first_name_value):
      self.first_name = first_name_value

  def set_last_name(self, last_name_value):
      self.last_name = last_name_value

  def display(self):
      print(f"First name: {self.first_name}, Last name: {self.last_name}")


""" Your code goes here """

  def __init__(self):
      DrinkOrder.__init__(self)

  def print_order(self):
      print("Milkshake")


first_name_value = input()
last_name_value = input()

customer_order = Milkshake()
customer_order.set_first_name(first_name_value)
customer_order.set_last_name(last_name_value)
customer_order.print_order()
customer_order.display()
'''

setin("Tia", "Lynn")
# val: None


class DrinkOrder:
    def __init__(self):
        self.first_name = 0
        self.last_name = 0

    def set_first_name(self, first_name_value):
        self.first_name = first_name_value

    def set_last_name(self, last_name_value):
        self.last_name = last_name_value

    def display(self):
        print(f"First name: {self.first_name}, Last name: {self.last_name}")
        # out: First name: Tia, Last name: Lynn


""" Your code goes here """


class Milkshake(DrinkOrder):
    def __init__(self):
        DrinkOrder.__init__(self)
        self.expiration = ""

    def __init__(self):
        DrinkOrder.__init__(self)
        # val: None

    def print_order(self):
        print("Milkshake")
        # out: Milkshake


first_name_value = input()
last_name_value = input()
# out: Tia
# out: Lynn
# out: Tia
# out: Lynn
# out: 16
# out: 3
# out: 500
# out: 270.0
# out: 215

customer_order = Milkshake()
customer_order.set_first_name(first_name_value)
# val: None
customer_order.set_last_name(last_name_value)
# val: None
customer_order.print_order()
# val: None
customer_order.display()
# val: None

'''challenge activity
13.1.2: Defining a derived class.
712910.5105864.qx3zqy7

Jump to level 1
Complete the definition of class Tea so that Tea is derived from the base class DrinkOrder.

class DrinkOrder:
    def __init__(self):
        self.first_name = 0
        self.last_name = 0

    def set_first_name(self, first_name_value):
        self.first_name = first_name_value

    def set_last_name(self, last_name_value):
        self.last_name = last_name_value

    def display(self):
        print(f"First name: {self.first_name}, Last name: {self.last_name}")


    """ Your code goes here """
    def __init__(self):
        DrinkOrder.__init__(self)

    def print_order(self):
        print("Tea")


first_name_value = input()
last_name_value = input()

customer_order = Tea()
customer_order.set_first_name(first_name_value)
customer_order.set_last_name(last_name_value)
customer_order.print_order()
customer_order.display()

 

1

2

3

Check

Next level
1
2
3

Feedback?'''

setin("Tia", "Lynn")
# val: None


class DrinkOrder:
    def __init__(self):
        self.first_name = 0
        self.last_name = 0

    def set_first_name(self, first_name_value):
        self.first_name = first_name_value

    def set_last_name(self, last_name_value):
        self.last_name = last_name_value

    def display(self):
        print(f"First name: {self.first_name}, Last name: {self.last_name}")
        # out: First name: Tia, Last name: Lynn

    """ Your code goes here """


class Tea(DrinkOrder):
    def __init__(self):
        DrinkOrder.__init__(self)
        self.expiration = ""

    def __init__(self):
        DrinkOrder.__init__(self)
        # val: None

    def print_order(self):
        print("Tea")
        # out: Tea


first_name_value = input()
last_name_value = input()

customer_order = Tea()
customer_order.set_first_name(first_name_value)
# val: None
customer_order.set_last_name(last_name_value)
# val: None
customer_order.print_order()
# val: None
customer_order.display()
# val: None


"""
challenge activity
13.1.2: Defining a derived class.
712910.5105864.qx3zqy7

Jump to level 1
Define the EnglishComposition class's __init__ method to explicitly call the base class's __init__ method.

Click here for example
Ex: If the input is:
16
3
then the output is:

English Composition
Duration: 16 weeks, Credits: 3

    def set_duration(self, duration_value):
        self.duration = duration_value

    def set_credits(self, credits_value):
        self.credits = credits_value




"""


def Q():
    class Course:
        def __init__(self):
            self.duration = 0
            self.credits = 0

        def set_duration(self, duration_value):
            self.duration = duration_value

        def set_credits(self, credits_value):
            self.credits = credits_value

        def display(self):
            print(f"Duration: {self.duration} weeks, Credits: {self.credits}")

    class EnglishComposition(Course):
        """Your code goes here"""

        def print_title(self):
            print("English Composition")

    duration_value = int(input())
    credits_value = int(input())

    my_job = EnglishComposition()
    my_job.set_duration(duration_value)
    my_job.set_credits(credits_value)
    my_job.print_title()
    my_job.display()


def A():
    class Course:
        def __init__(self):
            self.duration = 0
            self.credits = 0

        def set_duration(self, duration_value):
            self.duration = duration_value

        def set_credits(self, credits_value):
            self.credits = credits_value

        def display(self):
            print(f"Duration: {self.duration} weeks, Credits: {self.credits}")
            # out: Duration: 16 weeks, Credits: 3

    class EnglishComposition(Course):
        """Your code goes here"""

        def __init__(self):
            Course.__init__(self)
            # val: None
            self.expiration = ""

        def print_title(self):
            print("English Composition")
            # out: English Composition

    duration_value = int(input())
    credits_value = int(input())

    my_job = EnglishComposition()
    my_job.set_duration(duration_value)
    # val: None
    my_job.set_credits(credits_value)
    # val: None
    my_job.print_title()
    # val: None
    my_job.display()
    # val: None


setin("16", "3")
# val: None
A()
# val: None
"""challenge activity
13.1.2: Defining a derived class.
712910.5105864.qx3zqy7

Jump to level 1
Complete the definition of the Monkshood class as follows:

The Monkshood class is derived from the FlowerOrder class.
The Monkshood class's __init__ method explicitly calls the FlowerOrder class's __init__ method and then initializes the instance attribute named id with value 0.
Click here for example
Ex: If the input is:
500
270.00
215
then the output is:

Order ID: 0
Quantity: 500, Price: $270.00
Order ID: 215"""

setin(500, 270.00, 215)
# val: None


class FlowerOrder:
    def __init__(self):
        self.quantity = 0
        self.price = 0

    def set_quantity(self, quantity_value):
        self.quantity = quantity_value

    def set_price(self, price_value):
        self.price = price_value

    def display(self):
        print(f"Quantity: {self.quantity}, Price: ${self.price:.2f}")
        # out: Quantity: 500, Price: $270.00


class Monkshood(FlowerOrder):
    def __init__(self):
        FlowerOrder.__init__(self)
        # val: None
        self.id = 0
        self.expiration = ""

    def set_id(self, id_value):
        self.id = id_value

    def display_id(self):
        print(f"Order ID: {self.id}")
        # out: Order ID: 0
        # out: Order ID: 215


quantity_value = int(input())
price_value = float(input())
id_value = int(input())

bouquet_order = Monkshood()
bouquet_order.display_id()
# val: None

bouquet_order.set_quantity(quantity_value)
# val: None
bouquet_order.set_price(price_value)
# val: None
bouquet_order.set_id(id_value)
# val: None
bouquet_order.display()
# val: None
bouquet_order.display_id()
# val: None
