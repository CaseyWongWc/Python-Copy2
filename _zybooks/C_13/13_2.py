#save: _zybooks/C_13/13_2.py
from Helpers.helpings import *
'''13.2 Accessing base class attributes
A derived class can access the attributes of all of its base classes via normal attribute reference operations. For example, item1.set_name() might refer to the set_name method attribute of a class from which item1 is derived. An attribute reference is resolved using a search procedure that first checks the instance's namespace, then the classes' namespace, then the namespaces of any base classes.

The search for an attribute continues all the way up the inheritance tree, which is the hierarchy of classes from a derived class to the final base class. Ex: Consider the following class structure in which Motorcycle is derived from MotorVehicle, which is derived from TransportMode.

Figure 13.2.1: Searching the inheritance tree for an attribute.
class TransportMode:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def info(self):
        print(f"{self.name} can go {self.speed} mph.")

class MotorVehicle(TransportMode):
    def __init__(self, name, speed, mpg):
        TransportMode.__init__(self, name, speed)
        self.mpg = mpg
        self.fuel_gal = 0 

    def add_fuel(self, amount):
        self.fuel_gal += amount

    def drive(self, distance):
        required_fuel = distance / self.mpg
        if self.fuel_gal < required_fuel:
            print("Not enough gas.")
        else:
            self.fuel_gal -= required_fuel
            print(f"{self.fuel_gal:f} gallons remaining.")

class MotorCycle(MotorVehicle):
    def __init__(self, name, speed, mpg):
        MotorVehicle.__init__(self, name, speed, mpg)

    def wheelie(self):
        print("That is too dangerous.")


scooter = MotorCycle("Vespa", 55, 40)
dirtbike = MotorCycle("KX450F", 80, 25)

scooter.info()
dirtbike.info()
choice = input("Select scooter (s) or dirtbike (d): ")
bike = scooter if (choice == "s") else dirtbike

menu = "\nSelect add fuel(f), go(g), wheelie(w), quit(q): "
command = input(menu)
while command != "q":
    if command == "f":
        fuel = int(input("Enter amount: "))
        bike.add_fuel(fuel)
    elif command == "g":
        distance = int(input("Enter distance: "))
        bike.drive(distance)
    elif command == "w":
        bike.wheelie()
    elif command == "q":
        break
    else:
        print("Invalid command.")

    command = input(menu)
Vespa can go 55 mph.
KX450F can go 80 mph.
Select scooter (s) or dirtbike (d): d

Select add fuel(f), go(g), wheelie(w), quit(q): f
Enter amount: 3

Select add fuel(f), go(g), wheelie(w), quit(q): g
Enter distance: 60
0.600000 gallons remaining.

Select add fuel(f), go(g), wheelie(w), quit(q): g
Enter distance: 10
0.200000 gallons remaining.

Select add fuel(f), go(g), wheelie(w), quit(q): g
Enter distance: 25
Not enough gas.

# out: Select scooter (s) or dirtbike (d): d
# out: 
# out: Select add fuel(f), go(g), wheelie(w), quit(q): f
# out: Enter amount: 3
# out: 
# out: Select add fuel(f), go(g), wheelie(w), quit(q): g
# out: Enter distance: 60
# out: 
# out: Select add fuel(f), go(g), wheelie(w), quit(q): g
# out: Enter distance: 10
# out: 
# out: Select add fuel(f), go(g), wheelie(w), quit(q): g
# out: Enter distance: 25
# out: 
# out: Select add fuel(f), go(g), wheelie(w), quit(q): w
# out: 
# out: Select add fuel(f), go(g), wheelie(w), quit(q): q
Select add fuel(f), go(g), wheelie(w), quit(q): w
That is too dangerous.

Select add fuel(f), go(g), wheelie(w), quit(q): q'''
'''The above illustrates a program with three levels of inheritance. The scooter and dirt bike variables are instances of the Motorcycle class at the bottom of the inheritance tree. Calling the add_fuel() or drive() methods initiates a search, first in MotorCycle, and then in MotorVehicle. Calling the info() method defined at the top of the inheritance tree, as in scooter.info(), results in searching MotorCycle first, then MotorVehicle, and finally TransportMode.

Try 13.2.1: Extending the transportation modes class hierarchy.
class TransportMode:
  def __init__(self, name, speed):
      self.name = name
      self.speed = speed

  def info(self):
      print(f"{self.name} can go {self.speed} mph.")

class MotorVehicle(TransportMode):
  def __init__(self, name, speed, mpg):
      TransportMode.__init__(self, name, speed)
      self.mpg = mpg
      self.fuel_gal = 0

  def add_fuel(self, amount):
      self.fuel_gal += amount

  def drive(self, distance):
      required_fuel = distance / self.mpg
      if self.fuel_gal < required_fuel:
          print("Not enough gas.")
      else:
          self.fuel_gal -= required_fuel
          print(f"{self.fuel_gal:f} gallons remaining.")

class MotorCycle(MotorVehicle):
  def __init__(self, name, speed, mpg):
      MotorVehicle.__init__(self, name, speed, mpg)

  def wheelie(self):
      print("That is too dangerous.")

scooter = MotorCycle("Vespa", 55, 40)
dirtbike = MotorCycle("KX450F", 80, 25)

scooter.info()
dirtbike.info()
choice = input("Select scooter (s) or dirtbike (d): ")
bike = scooter if (choice == "s") else dirtbike

menu = "\nSelect add fuel(f), go(g), wheelie(w), quit(q): "
command = input(menu)
while command != "q":
  if command == "f":
      fuel = int(input("Enter amount: "))
      bike.add_fuel(fuel)
  elif command == "g":
      distance = int(input("Enter distance: "))
      bike.drive(distance)
  elif command == "w":
      bike.wheelie()
  elif command == "q":
      break
  else:
      print("Invalid command.")

  command = input(menu)
Full screen
Extend the above example with the following additional modes of transportation:

Implement an Airplane class that is derived from TransportMode. Airplane should have the methods add_fuel(), and fly(), and a data attribute num_passengers.
Implement a JetPlane class that is derived from Airplane. Add some methods to JetPlane of your own choosing, such as barrel_roll() or immelman().
'''
setin("d", "f", "3", "g", "60", "g", "10", "g", "25", "w", "q")
# val: None
class TransportMode:
  def __init__(self, name, speed):
      self.name = name
      self.speed = speed

  def info(self):
      print(f"{self.name} can go {self.speed} mph.")
      # out: Vespa can go 55 mph.
      # out: KX450F can go 80 mph.

class MotorVehicle(TransportMode):
  def __init__(self, name, speed, mpg):
      TransportMode.__init__(self, name, speed)
      # val: None
      # val: None
      self.mpg = mpg
      self.fuel_gal = 0

  def add_fuel(self, amount):
      self.fuel_gal += amount

  def drive(self, distance):
      required_fuel = distance / self.mpg
      if self.fuel_gal < required_fuel:
          print("Not enough gas.")
          # out: Not enough gas.
      else:
          self.fuel_gal -= required_fuel
          print(f"{self.fuel_gal:f} gallons remaining.")
          # out: 0.600000 gallons remaining.
          # out: 0.200000 gallons remaining.

class MotorCycle(MotorVehicle):
  def __init__(self, name, speed, mpg):
      MotorVehicle.__init__(self, name, speed, mpg)
      # val: None
      # val: None

  def wheelie(self):
      print("That is too dangerous.")
      # out: That is too dangerous.

scooter = MotorCycle("Vespa", 55, 40)
dirtbike = MotorCycle("KX450F", 80, 25)

scooter.info()
# val: None
dirtbike.info()
# val: None
choice = input("Select scooter (s) or dirtbike (d): ")
bike = scooter if (choice == "s") else dirtbike

menu = "\nSelect add fuel(f), go(g), wheelie(w), quit(q): "
command = input(menu)
while command != "q":
  if command == "f":
      fuel = int(input("Enter amount: "))
      bike.add_fuel(fuel)
      # val: None
  elif command == "g":
      distance = int(input("Enter distance: "))
      bike.drive(distance)
      # val: None
      # val: None
      # val: None
  elif command == "w":
      bike.wheelie()
      # val: None
  elif command == "q":
      break
  else:
      print("Invalid command.")

  command = input(menu)


'''participation activity
13.2.1: Searching for attributes in the inheritance tree.
1)T/F
"Inheritance tree" describes the hierarchy between base and derived classes.
2)T/F
Evaluating bike.wheelie() searches TransportMode, then MotorVehicle, then finally MotorCycle for the wheelie() method.
3)T/F
When adding a new derived class, a programmer has to change the base class as well.

Feedback?'''



