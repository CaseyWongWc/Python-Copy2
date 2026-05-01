# ===== 2026-05-01 02:40:34 | goog.py =====
"Figure 13.1.1: A derived class example: Class Produce is derived from class Items."


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
# ===== end =====

# ===== 2026-05-01 02:50:01 | goog.py =====

'''challenge activity
13.1.1: Derived classes.'''

class Vehicle:
    def __init__(self):
        self.speed = 0

    def set_speed(self, speed_to_set):
        self.speed = speed_to_set

    def print_speed(self):
        print(self.speed)
        # out: 30


class Car(Vehicle):
    def print_car_speed(self):
        print("Moving at: ", end = "")
        # out: Moving at: 
        self.print_speed()
        # val: None


myCar = Car()
myCar.set_speed(30)
# val: None
myCar.print_car_speed()
# val: None
# ===== end =====

# ===== 2026-05-01 03:05:37 | goog.py =====
from Helpers.helpings import *

'''challenge activity
13.1.1: Derived classes.'''

class Vehicle:
    def __init__(self):
        self.speed = 0

    def set_speed(self, speed_to_set):
        self.speed = speed_to_set

    def print_speed(self):
        print(self.speed)
        # out: 20
        # out: 9


class Car(Vehicle):
    def print_car_speed(self):
        print("Moving at: ", end = "")
        # out: Moving at: 
        self.print_speed()
        # val: None


class AnimalPowered(Vehicle):
    def __init__(self):
        self.animal = ""

    def set_animal(self, animal_to_set):
        self.animal = animal_to_set

    def print_animal_speed(self):
        print(f"{self.animal} speed: ", end = "")
        # out: Donkey speed: 
        self.print_speed()
        # val: None


myCar = Car()
chariot = AnimalPowered()

myCar.set_speed(20)
# val: None
chariot.set_speed(9)
# val: None
chariot.set_animal("Donkey")
# val: None

myCar.print_car_speed()
# val: None
chariot.print_animal_speed()
# val: None

'''	
Moving at: 20
Donkey speed: 9

'''





def CA_13_1_1_3():
    class Vehicle:
      def __init__(self):
          self.speed = 0

      def set_speed(self, speed_to_set):
          self.speed = speed_to_set

      def print_speed(self):
          print(self.speed)
          # out: 20


    class Car(Vehicle):
      def print_car_speed(self):
          print("Moving at: ", end = "")
          # out: Moving at: 
          self.print_speed()
          # val: None


    class ElectricCar(Car):
      def __init__(self):
          self.battery_level = 0

      def set_battery_level(self, level_to_set):
          self.battery_level = level_to_set

      def print_battery_level(self):
          print(f"Battery: {self.battery_level}")
          # out: Battery: 10


    myCar = ElectricCar()
    myCar.set_speed(20)
    # val: None
    myCar.set_battery_level(10)
    # val: None

    myCar.print_car_speed()
    # val: None
    myCar.print_battery_level()
    # val: None
CA_13_1_1_3()
# val: None
# ===== end =====
