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

Milkshake
First name: Tia, Last name: Lynn
 

1

2

3

Check

Next level
1
2
3

Feedback?'''
class Temp:
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