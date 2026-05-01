########################################################################################################
'''Activity summary for assignment: C_11
32 / 85 points
Due: 05/07/2026, 11:59 PM PDT

Completion details
Section 13.1
11 / 11 points

P
Participation activities
13.1.1
1 / 1 point
13.1.2
1 / 1 point
13.1.3
1 / 1 point
13.1.4
2 / 2 points
C
Challenge activities
13.1.1
3 / 3 points
13.1.2
3 / 3 points
Section 13.2
5 / 5 points

P
Participation activities
13.2.1
3 / 3 points
C
Challenge activities
13.2.1
2 / 2 points
Section 13.3
8 / 8 points

P
Participation activities
13.3.1
4 / 4 points
C
Challenge activities
13.3.1
1 / 1 point
13.3.2
3 / 3 points
Section 13.4
6 / 6 points

P
Participation activities
13.4.1
4 / 4 points
C
Challenge activities
13.4.1
2 / 2 points
Section 13.5
2 / 2 points

P
Participation activities
13.5.1
1 / 1 point
13.5.2
1 / 1 point
Section 13.6
0 / 3 points

P
Participation activities
13.6.1
0 / 3 points
Next section
Section 13.7
0 / 10 points

L
Lab activities
13.7.1
0 / 10 points
Section 13.8
0 / 10 points

L
Lab activities
13.8.1
0 / 10 points
Section 13.9
0 / 10 points

L
Lab activities
13.9.1
0 / 10 points
Section 13.10
0 / 10 points

L
Lab activities
13.10.1
0 / 10 points
Section 13.11
0 / 10 points

L
Lab activities
13.11.1
0 / 10 points
'''
########################################################################################################

####################################################13.1 Derived classes

'''A class will commonly share attributes with another class, but with some additions or variations. Ex: A store inventory system might use a class called Item, having name and quantity attributes. But for fruits and vegetables, a class Produce might have the attributes name, quantity, and expiration date. Note that Produce is really an Item with an additional feature, so ideally a program could define the Produce class as being the same as the Item class but with the addition of an expiration date attribute.

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

Feedback?
The example defines a class named Item. In the script, an instance of Item is created called item1, the instance's attributes are set to Smith Cereal and 9, and the display() method is called. A class named Produce is also defined. That class was derived from the Item class by including the base class Item within parentheses after Produce. Ex: class Produce(Item):. As such, instantiating a Produce instance item2 creates an instance object with the data attributes name and quantity (from Item), plus expiration (from Produce), as well as with the methods set_name(), set_quantity(), and display() from Item, and set_expiration() and get_expiration() from Produce. In the script, item2 has instance data attributes set to Apples, 40, and May 5, 2012. The display() method is called, and then the expiration date is printed using the get_expiration() method.interfaces

All of the class attributes of Item are available to instances of Produce, though instance attributes are not. The __init__ method of Item must be explicitly called in the constructor of Produce, Ex: Item.__init__(self), so that the instance of Produce is assigned the name and quantity data attributes. When an instantiation of a Produce instance occurs, Produce.__init__() executes and immediately calls Item.__init__(). The newly created Produce instance is passed as the first argument (self) to the Item constructor, which creates the name and quantity attributes in the new Item instance's namespace. Item.__init__() returns, and Produce.__init__() continues, creating the expiration attribute. The following tool illustrates:

PythonTutor: Derived class explicitly calls base class' constructor.


Feedback?
The term derived class refers to a class that inherits the class attributes of another class, known as a base class. Any class may serve as a base class; no changes to the definition of that class are required. The derived class is said to inherit the attributes of its base class, a concept called inheritance. An instance of a derived class type has access to all the attributes of the derived class as well as the class attributes of the base class by default, including the base class's methods. A derived class instance can simulate inheritance of instance attributes as well by calling the base class constructor manually. The following animation illustrates the relationship between a derived class and a base class.

participation activity
13.1.1: Derived class example: Produce derived from Item.

Start
item1 = Item()
item2 = Produce()

# ...
ItemProduceitem1item2.......................................................Access to:Access to:ProduceItemname
quantity
display()
set_name()
set_quantity()
name
quantity
display()
expiration
set_name()
set_quantity()
get_expiration()
set_expiration()
Static Figure: Begin Python code: item1 = Item() item2 = Produce() # ... End Python code. Produce is derived from Item. item1 has access to name, quantity, display(), set_name(), set_quantity(). item2 has access to name, quantity, expiration, display(), set_name(), set_quantity(), get_expiration(), set_expiration(). Step 1: Item is the base class. The line of code item1 = Item() is highlighted. item1 has access to name, quantity, display(), set_name(), set_quantity(). Step 2: Produce is derived so Produce inherits Item's attributes. The line of code item2 = Produce() is highlighted. item2 has access to name, quantity, expiration, display(), set_name(), set_quantity(), get_expiration(), set_expiration().

Captions
Item is the base class.
Produce is derived so Produce inherits Item's attributes.

Feedback?
The inheritance relationship is commonly drawn as follows, using Unified Modeling Language (UML) notation (Wikipedia: UML).

participation activity
13.1.2: UML derived class example: Produce derived from Item.

Start
Item+name+quantity+set_name()+set_quantity()+display()Produce+expiration+set_expiration()+get_expiration()Member access
- means private
+ means public
# means protected
class name
data
members
methods
Static figure: Item has public data members name, quantity, and public methods set_name(), set_quantity(), display(). Produce is derived from Item and has the same data members and methods along with additional public data members expiration, and public methods set_expiration(), and get_expiration(). In UML, member access is described by -, which means private, +, which means public and #, which means protected. Step 1: A class diagram depicts a class' name, data members, and methods. The class name is Item. The data members are name and quantity and are public. The methods are set_name(), set_quantity(), and display(), and are public. Step 2: A solid line with a closed, unfilled arrowhead indicates a class is derived from another class. Produce is derived from Item. Step 3: The derived class shows only additional members. Produce has an additional data member expiration which is public. Produce has additional methods set_expiration() and get_expiration() which are public.

Captions
A class diagram depicts a class' name, data members, and methods.
A solid line with a closed, unfilled arrowhead indicates a class is derived from another class.
The derived class shows only additional members.

Feedback?
In the above animation, the +, -, and # symbols refer to the access level of an attribute. Ex: Whether or not that attribute can be accessed by anyone (public), only instances of that class (private), or instances derived from that class (protected), respectively. In Python, all attributes are public.privacy. Many languages, such as Java, C, and C++, explicitly require setting access levels on every variable and function in a class, thus UML as a language-independent tool includes the symbols.

Various class derivation variations are possible:

A derived class can itself serve as a base class for another class. In the earlier example, "class Fruit(Produce):" could be added.
A class can serve as a base class for multiple derived classes. In the earlier example, "class Book(Item):" could be added.
A class may be derived from multiple classes. For example, "class House(Dwelling, Property):" could be defined.
participation activity
13.1.3: Interactive inheritance tree.
Click a class to see available methods and data for that class.

Inheritance tree	Selected class pseudocode
Item
                             
Produce                                    Book
                                                                   
Fruit Dairy               Textbook Audiobook	
    def set_name(self, nm):
    def set_quantity(self, qnty):
    def display(self):




Data attributes:
    self.name
    self.quantity


Selected class code
class Item:
    def __init__(self):
        self.name = ""
        self.quantity = 0

    def set_name(self, nm):
        self.name = nm

    def set_quantity(self, qnty):
        self.quantity = qnty

    def display(self):
        # print name, quantity


'''
##########################
'''participation activity
13.1.4: Derived classes basics.
1)
A class that can serve as the basis for another class is called a _______ class.

Check

Show answer
2)
Class "Dwelling" has the method open_door(). Class "House" is derived from Dwelling and has the methods open_window() and open_basement(). After h = House() executes, how many different methods can h call, ignoring constructors?

Check

Show answer

Feedback?'''
{
    {
        "A class that can serve as the basis for another class is called a _______ class.",
        "base"
    },
    {
        "Class \"Dwelling\" has the method open_door(). Class \"House\" is derived from Dwelling and has the methods open_window() and open_basement(). After h = House() executes, how many different methods can h call, ignoring constructors?",
        "3"
    }
}
#?
#-base class ex
class Dwelling:
    def open_door(self):
        pass
#
#?
class Dwelling:
    def open_door(self):
        pass
class House(Dwelling):
    def open_window(self):
        pass
    def open_basement(self):
        pass
h = House()
# h can call open_door(), open_window(), and open_basement()
##########################
'''challenge activity
13.1.1: Derived classes.
712910.5105864.qx3zqy7
Jump to level 1
Type the program's output

class Vehicle:
    def __init__(self):
        self.speed = 0

    def set_speed(self, speed_to_set):
        self.speed = speed_to_set

    def print_speed(self):
        print(self.speed)


class Car(Vehicle):
    def print_car_speed(self):
        print("Speed: ", end = "")
        self.print_speed()


myCar = Car()
myCar.set_speed(55)
myCar.print_car_speed()
1
2
3
Check
Next
1
2
3

Feedback?'''
class Vehicle:
    def __init__(self):
        self.speed = 0

    def set_speed(self, speed_to_set):
        self.speed = speed_to_set

    def print_speed(self):
        print(self.speed)


class Car(Vehicle):
    def print_car_speed(self):
        print("Speed: ", end = "")
        self.print_speed()


myCar = Car()
myCar.set_speed(55)
myCar.print_car_speed()
#Output:
"""Speed: 55

"""
##########################
'''challenge activity
13.1.1: Derived classes.
712910.5105864.qx3zqy7
Jump to level 1
Type the program's output

class Vehicle:
    def __init__(self):
        self.speed = 0

    def set_speed(self, speed_to_set):
        self.speed = speed_to_set

    def print_speed(self):
        print(self.speed)


class Car(Vehicle):
    def print_car_speed(self):
        print("Moving at: ", end = "")
        self.print_speed()


myCar = Car()
myCar.set_speed(55)
myCar.print_car_speed()
#Output:
'''
class Vehicle:
    def __init__(self):
        self.speed = 0

    def set_speed(self, speed_to_set):
        self.speed = speed_to_set

    def print_speed(self):
        print(self.speed)


class Car(Vehicle):
    def print_car_speed(self):
        print("Moving at: ", end = "")
        self.print_speed()


myCar = Car()
myCar.set_speed(55)
myCar.print_car_speed()
#Output:
'''Moving at: 55

'''
##########################
'''challenge activity
13.1.1: Derived classes.
712910.5105864.qx3zqy7
Jump to level 1
Type the program's output'''

class Vehicle:
    def __init__(self):
        self.speed = 0

    def set_speed(self, speed_to_set):
        self.speed = speed_to_set

    def print_speed(self):
        print(self.speed)


class Car(Vehicle):
    def print_car_speed(self):
        print("Driving at: ", end = "")
        self.print_speed()


class AnimalPowered(Vehicle):
    def __init__(self):
        self.animal = ""

    def set_animal(self, animal_to_set):
        self.animal = animal_to_set

    def print_animal_speed(self):
        print(f"{self.animal} speed: ", end = "")
        self.print_speed()


myCar = Car()
chariot = AnimalPowered()

myCar.set_speed(20)
chariot.set_speed(12)
chariot.set_animal("Donkey")

myCar.print_car_speed()
chariot.print_animal_speed()

#Output:
'''Driving at: 20
Donkey speed: 12
'''
##########################
'''challenge activity
13.1.1: Derived classes.
712910.5105864.qx3zqy7
Jump to level 1
Type the program's output'''

class Vehicle:
    def __init__(self):
        self.speed = 0

    def set_speed(self, speed_to_set):
        self.speed = speed_to_set

    def print_speed(self):
        print(self.speed)


class Car(Vehicle):
    def print_car_speed(self):
        print("Moving at: ", end = "")
        self.print_speed()


class ElectricCar(Car):
    def __init__(self):
        self.battery_level = 0

    def set_battery_level(self, level_to_set):
        self.battery_level = level_to_set

    def print_battery_level(self):
        print(f"Battery: {self.battery_level}")


myCar = ElectricCar()
myCar.set_speed(60)
myCar.set_battery_level(5)

myCar.print_car_speed()
myCar.print_battery_level()

#Output:
'''Moving at: 60
Battery: 5
'''
##########################
'''challenge activity
13.1.2: Defining a derived class.
712910.5105864.qx3zqy7

Jump to level 1
Complete the definition of class Daffodil so that Daffodil is derived from the base class FlowerOrder.

Click here for example
Ex: If the input is:
250
85.00
then the output is:

Daffodil
Quantity: 250, Price: $85.00'''
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


""" Your code goes here """
class Daffodil(FlowerOrder):
    def __init__(self):
        FlowerOrder.__init__(self)

    def print_order(self):
        print("Daffodil")


quantity_value = int(input())
price_value = float(input())

bouquet_order = Daffodil()
bouquet_order.set_quantity(quantity_value)
bouquet_order.set_price(price_value)
bouquet_order.print_order()
bouquet_order.display()

'''challenge activity
13.1.2: Defining a derived class.
712910.5105864.qx3zqy7

Jump to level 1
Define the BusinessAnalyst class's __init__ method to explicitly call the base class's __init__ method.

Click here for example
Ex: If the input is:
2005
3
then the output is:

Business Analyst
Start year: 2005, Level: 3
'''
class Job:
    def __init__(self):
        self.start_year = 0
        self.level = 0

    def set_start_year(self, start_year_value):
        self.start_year = start_year_value

    def set_level(self, level_value):
        self.level = level_value

    def display(self):
        print(f"Start year: {self.start_year}, Level: {self.level}")


class BusinessAnalyst(Job):

    """ Your code goes here """
    def __init__(self):
        Job.__init__(self)

    def print_title(self):
        print("Business Analyst")


start_year_value = int(input())
level_value = int(input())

my_job = BusinessAnalyst()
my_job.set_start_year(start_year_value)
my_job.set_level(level_value)
my_job.print_title()
my_job.display()
##########################
'''activity
13.1.2: Defining a derived class.
712910.5105864.qx3zqy7

Jump to level 1
Complete the definition of the Ageratum class as follows:

The Ageratum class is derived from the FlowerOrder class.
The Ageratum class's __init__ method explicitly calls the FlowerOrder class's __init__ method and then initializes the instance attribute named id with value 0.
Click here for example
Ex: If the input is:
150
185.00
465
then the output is:

Order ID: 0
Quantity: 150, Price: $185.00
Order ID: 465
'''
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


""" Your code goes here """
class Ageratum(FlowerOrder):
    def __init__(self):
        FlowerOrder.__init__(self)
        self.id = 0

    def set_id(self, id_value):
        self.id = id_value

    def display_id(self):
        print(f"Order ID: {self.id}")


quantity_value = int(input())
price_value = float(input())
id_value = int(input())

flower_order = Ageratum()
flower_order.display_id()

flower_order.set_quantity(quantity_value)
flower_order.set_price(price_value)
flower_order.set_id(id_value)
flower_order.display()
flower_order.display_id()
####################################################13.2 Accessing base class attributes
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

Select add fuel(f), go(g), wheelie(w), quit(q): w
That is too dangerous.

Select add fuel(f), go(g), wheelie(w), quit(q): q

Feedback?
The above illustrates a program with three levels of inheritance. The scooter and dirt bike variables are instances of the Motorcycle class at the bottom of the inheritance tree. Calling the add_fuel() or drive() methods initiates a search, first in MotorCycle, and then in MotorVehicle. Calling the info() method defined at the top of the inheritance tree, as in scooter.info(), results in searching MotorCycle first, then MotorVehicle, and finally TransportMode.

Try 13.2.1: Extending the transportation modes class hierarchy.

Full screen
Extend the above example with the following additional modes of transportation:

Implement an Airplane class that is derived from TransportMode. Airplane should have the methods add_fuel(), and fly(), and a data attribute num_passengers.
Implement a JetPlane class that is derived from Airplane. Add some methods to JetPlane of your own choosing, such as barrel_roll() or immelman().


Feedback?
participation activity
13.2.1: Searching for attributes in the inheritance tree.
1)
"Inheritance tree" describes the hierarchy between base and derived classes.
2)
Evaluating bike.wheelie() searches TransportMode, then MotorVehicle, then finally MotorCycle for the wheelie() method.
3)
When adding a new derived class, a programmer has to change the base class as well.

Feedback?
challenge activity
13.2.1: Accessing base class attributes.
712910.5105864.qx3zqy7
Start
Select the attributes that
my_vehicle can access.class Property:
    def __init__(self, owner):
        self.owner = owner


class Scarf(Property):
    def __init__(self, owner, color):
        Property.__init__(self, owner)
        self.color = color

    def info(self):
        print(f"{self.owner}'s scarf is {self.color}.")


class Boat(Property):
    def __init__(self, owner, tag):
        Property.__init__(self, owner)
        self.tag = tag

    def info(self):
        print(f"{self.owner}'s boat has tag {self.tag}.")


my_vehicle = Boat("Tim", "C65874")
1
2
Check
Next
1
2

Feedback?
How was this section?

|


Provide section feedback'''
##########################Figure 13.2.1: Searching the inheritance tree for an attribute.
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

    ##########################Try 13.2.1: Extending the transportation modes class hierarchy.
    '''Extend the above example with the following additional modes of transportation:

Implement an Airplane class that is derived from TransportMode. Airplane should have the methods add_fuel(), and fly(), and a data attribute num_passengers.
Implement a JetPlane class that is derived from Airplane. Add some methods to JetPlane of your own choosing, such as barrel_roll() or immelman().'''
#=
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
#=
##########################
'''participation activity

## 

13.2.1: Searching for attributes in the inheritance tree.

1)

"Inheritance tree" describes the hierarchy between base and derived classes.

True

False

2)

Evaluating bike.wheelie() searches TransportMode, then MotorVehicle, then finally MotorCycle for the wheelie() method.

True

False

3)

When adding a new derived class, a programmer has to change the base class as well.

True

False

Feedback?'''

{
    {
        "\"Inheritance tree\" describes the hierarchy between base and derived classes.",
        "True"
    },
    {
        "Evaluating bike.wheelie() searches TransportMode, then MotorVehicle, then finally MotorCycle for the wheelie() method.",
        "False"
    },
    {
        "When adding a new derived class, a programmer has to change the base class as well.",
        "False"
    }
}
##########################
'''challenge activity
13.2.1: Accessing base class attributes.
712910.5105864.qx3zqy7
Jump to level 1
Select the attributes that
my_vehicle can access.class Property:
    def __init__(self, owner):
        self.owner = owner


class Scarf(Property):
    def __init__(self, owner, color):
        Property.__init__(self, owner)
        self.color = color

    def info(self):
        print(f"{self.owner}'s scarf is {self.color}.")


class Boat(Property):
    def __init__(self, owner, tag):
        Property.__init__(self, owner)
        self.tag = tag

    def info(self):
        print(f"{self.owner}'s boat has tag {self.tag}.")


my_vehicle = Boat("Tim", "C65874")
1
2
Check
Next
1
2

Feedback?'''
class Property:
    def __init__(self, owner):
        self.owner = owner


class Scarf(Property):
    def __init__(self, owner, color):
        Property.__init__(self, owner)
        self.color = color

    def info(self):
        print(f"{self.owner}'s scarf is {self.color}.")


class Boat(Property):
    def __init__(self, owner, tag):
        Property.__init__(self, owner)
        self.tag = tag

    def info(self):
        print(f"{self.owner}'s boat has tag {self.tag}.")


my_vehicle = Boat("Tim", "C65874")

{
    "owner",
    "tag",
    "info()"
}
##########################
'''challenge activity
13.2.1: Accessing base class attributes.
712910.5105864.qx3zqy7
Jump to level 1
Determine the order of search
when my_clothes.info() is evaluated.class Property:
    def __init__(self, owner):
        self.owner = owner

    def info(self):
        print(f"Owner is {self.owner}.")


class Clothes(Property):
    def __init__(self, owner, count):
        Property.__init__(self, owner)
        self.count = count

    def info(self):
        print(f"{self.owner} has {self.count} items of clothing.")


class Shirt(Clothes):
    def __init__(self, owner, count, color):
        Clothes.__init__(self, owner, count)
        self.color = color


my_clothes = Shirt("Ike", 7, "red")
my_clothes.info()PropertyClothesShirt
Pick

Pick

Pick
1
2
Check
Next
1
'''

class Property:
    def __init__(self, owner):
        self.owner = owner

    def info(self):
        print(f"Owner is {self.owner}.")


class Clothes(Property):
    def __init__(self, owner, count):
        Property.__init__(self, owner)
        self.count = count

    def info(self):
        print(f"{self.owner} has {self.count} items of clothing.")


class Shirt(Clothes):
    def __init__(self, owner, count, color):
        Clothes.__init__(self, owner, count)
        self.color = color


my_clothes = Shirt("Ike", 7, "red")
my_clothes.info()

# The search order is Shirt, then Clothes, and finally Property is  Not searched.
{
    "Shirt",
    "Clothes",
    "Property Not searched",
}
####################################################13.3 Overriding base class attributes
'''13.3 Overriding class methods
A derived class may define a method having the same name as a method in the base class. Such a member function overrides the method of the base class. The following example shows the earlier Item/Produce example where the Produce class has its own display() method that overrides the display() method of the Item class.

Figure 13.3.1: Produce's display() function overrides Item's display() function.
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

   def display(self):
       print(self.name, self.quantity, end=" ")
       print(f"  (Expires: {self.expiration})")


item1 = Item()
item1.set_name("Smith Cereal")
item1.set_quantity(9)
item1.display()  # Will call Item's display()

item2 = Produce()
item2.set_name("Apples")
item2.set_quantity(40)
item2.set_expiration("May 5, 2012")
item2.display()  # Will call Produce's display()
Smith Cereal 9
Apples 40   (Expires: May 5, 2012)

Feedback?
When the derived class defines the method being overwritten, that method is placed in the class's namespace. Because attribute references search the inheritance tree by starting with the derived class and then recursively searching base classes, the method called will always be the method defined in the instance's class.

A programmer will often want to extend, rather than replace, the base class method. The base class method can be explicitly called at the start of the method, with the derived class then performing additional operations:

Figure 13.3.2: Method calling overridden method of base class.
class Produce(Item):
    # ...
    def display(self):
        Item.display(self)
        print(f"  (Expires: {self.expiration})")
    # ...

Feedback?
Above, the display() method of Produce calls the display() method of Item, passing self as the first argument. Thus, when Item's display() executes, the name and quantity instance attributes from the Produce instance are retrieved and printed.

participation activity
13.3.1: Overriding base class methods.
Assume my_item is an instance of Item, and my_produce is an instance of Produce, with classes Item and Produce defined as above.

1)
Will my_item.display() call the display() function for Item or for Produce?

Check

Show answer
2)
Will my_produce.display() call the display() function for Item or for Produce?

Check

Show answer
3)
Provide a statement within the display() method of the Produce class to call the display() method of Produce's base class.

Check

Show answer
4)
If Produce did NOT have its own display() method defined, the display method of which class would be called in the following code? Type "ERROR" if appropriate.
p = Produce()
p.display()

Check

Show answer

Feedback?
challenge activity
13.3.1: Basic derived class member override.

Full screen
712910.5105864.qx3zqy7
Organize the lines of code to define a member method print_all() for class PetData. Make use of the base class's print_all() method.

Ex: If the input is:

Fluffy
5
4444

then the output is:

Name: Fluffy
Age: 5
ID: 4444

Note: Not all lines of code on the left should be used in the final solution.


How to use this tool
Unused
main.py

Load default template...
    
    

Check

Feedback?
challenge activity
13.3.2: Overriding class methods.
712910.5105864.qx3zqy7

Start
In the SalesRepresentative class, complete the definition of the method that overrides the Job class's display() method.

Click here for example
 

1

2

3

Check

Next level
1
2
3

Feedback?
How was this section?

|


Provide section feedback'''
##########################Figure 13.3.1: Produce's display() function overrides Item's display() function.
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

   def display(self):
       print(self.name, self.quantity, end=" ")
       print(f"  (Expires: {self.expiration})")


item1 = Item()
item1.set_name("Smith Cereal")
item1.set_quantity(9)
item1.display()  # Will call Item's display()

item2 = Produce()
item2.set_name("Apples")
item2.set_quantity(40)
item2.set_expiration("May 5, 2012")
item2.display()  # Will call Produce's display()
##########################Figure 13.3.2: Method calling overridden method of base class.
class Produce(Item):
    # ...
    def display(self):
        Item.display(self)
        print(f"  (Expires: {self.expiration})")
    # ...
##########################
'''participation activity
13.3.1: Overriding base class methods.
Assume my_item is an instance of Item, and my_produce is an instance of Produce, with classes Item and Produce defined as above.

1)
Will my_item.display() call the display() function for Item or for Produce?

Check

Show answer
2)
Will my_produce.display() call the display() function for Item or for Produce?

Check

Show answer
3)
Provide a statement within the display() method of the Produce class to call the display() method of Produce's base class.

Check

Show answer
4)
If Produce did NOT have its own display() method defined, the display method of which class would be called in the following code? Type "ERROR" if appropriate.
p = Produce()
p.display()

Check

Show answer

Feedback?'''
{
    {
        "Will my_item.display() call the display() function for Item or for Produce?",
        "Item"
    },
    {
        "Will my_produce.display() call the display() function for Item or for Produce?",
        "Produce"
    },
    {
        "Provide a statement within the display() method of the Produce class to call the display() method of Produce's base class.",
        "Item.display(self)"
    },
    {
        "If Produce did NOT have its own display() method defined, the display method of which class would be called in the following code? Type \"ERROR\" if appropriate.\np = Produce()\np.display()",
        "Item"
    }
}
##########################
'''challenge activity
13.3.1: Basic derived class member override.

Full screen
712910.5105864.qx3zqy7
Organize the lines of code to define a member method print_all() for class PetData. Make use of the base class's print_all() method.

Ex: If the input is:

Fluffy
5
4444

then the output is:

Name: Fluffy
Age: 5
ID: 4444

Note: Not all lines of code on the left should be used in the final solution.


How to use this tool
Unused
main.py

Load default template...
    
    
#### main.py

Load default template...

class AnimalData: def \_\_init\_\_(self): self.full\_name = "" self.age\_years = 0 def set\_name(self, given\_name): self.full\_name = given\_name def set\_age(self, num\_years): self.age\_years = num\_years \# Other parts omitted def print\_all(self): print(f"Name: {self.full\_name}") print(f"Age: {self.age\_years}") class PetData(AnimalData): def \_\_init\_\_(self): AnimalData.\_\_init\_\_(self) self.id\_num = 0 def set\_id(self, pet\_id): self.id\_num = pet\_id \# FIXME: Add print\_all() member method

user\_pet = PetData() user\_pet.set\_name(input()) user\_pet.set\_age(int(input())) user\_pet.set\_id(int(input())) user\_pet.print\_all()

Check

Feedback?
Check

Feedback?'''
class AnimalData:
    def __init__(self):
        self.full_name = ""
        self.age_years = 0

    def set_name(self, given_name):
        self.full_name = given_name

    def set_age(self, num_years):
        self.age_years = num_years

    # Other parts omitted
    def print_all(self):
        print(f"Name: {self.full_name}")
        print(f"Age: {self.age_years}")
class PetData(AnimalData):
    def __init__(self):
        AnimalData.__init__(self)
        self.id_num = 0

    def set_id(self, pet_id):
        self.id_num = pet_id

    def print_all(self):
        AnimalData.print_all(self)
        print(f"ID: {self.id_num}")
##########################
'''challenge activity
13.3.2: Overriding class methods.
712910.5105864.qx3zqy7

Jump to level 1
In the SalesRepresentative class, complete the definition of the method that overrides the Job class's display() method.

Click here for example
Ex: If the input is:
2013
1

then the output is:

Job title: Sales Representative, Start year: 2013, Level: 1
class Job:
    def __init__(self):
        self.start_year = 0
        self.level = 0

    def set_start_year(self, start_year_value):
        self.start_year = start_year_value

    def set_level(self, level_value):
        self.level = level_value

    def display(self):
        print(f"Start year: {self.start_year}, Level: {self.level}")


class SalesRepresentative(Job):
    def __init__(self):
        Job.__init__(self)

    """ Your code goes here """:
        print(f"Job title: Sales Representative, Start year: {self.start_year}, Level: {self.level}")


start_year_value = int(input())
level_value = int(input())

current_job = SalesRepresentative()
current_job.set_start_year(start_year_value)
current_job.set_level(level_value)
current_job.display()
'''
class Job:
    def __init__(self):
        self.start_year = 0
        self.level = 0

    def set_start_year(self, start_year_value):
        self.start_year = start_year_value

    def set_level(self, level_value):
        self.level = level_value

    def display(self):
        print(f"Start year: {self.start_year}, Level: {self.level}")


class SalesRepresentative(Job):
    def __init__(self):
        Job.__init__(self)

    def display(self):
        print(f"Job title: Sales Representative, Start year: {self.start_year}, Level: {self.level}")


start_year_value = int(input())
level_value = int(input())

current_job = SalesRepresentative()
current_job.set_start_year(start_year_value)
current_job.set_level(level_value)
current_job.display()
##########################
'''challenge activity
13.3.2: Overriding class methods.
712910.5105864.qx3zqy7

Jump to level 1
In the class SpeechTherapist's display() method:

Output "Job title: Speech Therapist".
Call the Job class's display() method.
Click here for example
Ex: If the input is:
2008
1

then the output is:

Job title: Speech Therapist
Start year: 2008, Level: 1
class Job:
    def __init__(self):
        self.start_year = 0
        self.level = 0

    def set_start_year(self, start_year_value):
        self.start_year = start_year_value

    def set_level(self, level_value):
        self.level = level_value

    def display(self):
        print(f"Start year: {self.start_year}, Level: {self.level}")


class SpeechTherapist(Job):
    def __init__(self):
        Job.__init__(self)

    def display(self):

        """ Your code goes here """


start_year_value = int(input())
level_value = int(input())

your_job = SpeechTherapist()
your_job.set_start_year(start_year_value)
your_job.set_level(level_value)
your_job.display()
'''
class Job:
    def __init__(self):
        self.start_year = 0
        self.level = 0

    def set_start_year(self, start_year_value):
        self.start_year = start_year_value

    def set_level(self, level_value):
        self.level = level_value

    def display(self):
        print(f"Start year: {self.start_year}, Level: {self.level}")


class SpeechTherapist(Job):
    def __init__(self):
        Job.__init__(self)

    def display(self):
        """ Your code goes here """
        print(f"Job title: Speech Therapist")
        Job.display(self)


start_year_value = int(input())
level_value = int(input())

your_job = SpeechTherapist()
your_job.set_start_year(start_year_value)
your_job.set_level(level_value)
your_job.display()
##########################
'''challenge activity
13.3.2: Overriding class methods.
712910.5105864.qx3zqy7

Jump to level 1
In the class Immunology, define a output() method to override the Course class's output() method and:

Call the Course class's output() method.
Output "Course name: Immunology".
Click here for example
Ex: If the input is:
9
2

then the output is:

Duration: 9 weeks, Credits: 2
Course name: Immunology
class Course:
    def __init__(self):
        self.duration = 0
        self.credits = 0

    def set_duration(self, duration_value):
        self.duration = duration_value

    def set_credits(self, credits_value):
        self.credits = credits_value

    def output(self):
        print(f"Duration: {self.duration} weeks, Credits: {self.credits}")


class Immunology(Course):
    def __init__(self):
        Course.__init__(self)

    """ Your code goes here """


duration_value = int(input())
credits_value = int(input())

winter_class = Immunology()
winter_class.set_duration(duration_value)
winter_class.set_credits(credits_value)
winter_class.output()
'''
class Course:
    def __init__(self):
        self.duration = 0
        self.credits = 0

    def set_duration(self, duration_value):
        self.duration = duration_value

    def set_credits(self, credits_value):
        self.credits = credits_value

    def output(self):
        print(f"Duration: {self.duration} weeks, Credits: {self.credits}")


class Immunology(Course):
    def __init__(self):
        Course.__init__(self)

    """ Your code goes here """
    def output(self):
        Course.output(self)
        print(f"Course name: Immunology")


duration_value = int(input())
credits_value = int(input())

winter_class = Immunology()
winter_class.set_duration(duration_value)
winter_class.set_credits(credits_value)
winter_class.output()
####################################################13.4 Is-a versus has-a relationships
'''13.4 Is-a versus has-a relationships
The concept of inheritance is often confused with composition. Composition is the idea that one object may be made up of other objects. For instance, a "mother" class can be made up of objects like "name" (possibly a string object), "children" (which may be a list of Child objects), etc. Defining that "mother" class does not involve inheritance, but rather just composing the sub-objects in the class.

Figure 13.4.1: Composition.
The 'has-a' relationship. A Mother object 'has-a' string object and 'has' child objects, but no inheritance is involved.

class Child:
    def __init__(self):
        self.name = ""
        self.birthdate = ""
        self.schoolname = ""
    # ...

class Mother:
    def __init__(self):
        self.name = ""
        self.birthdate = ""
        self.spouse_name = ""
        self.children = []
    # ...

Feedback?
In contrast, a programmer may note that a mother and a child are both a kind of person, and all persons have a name and birthdate. So the programmer may decide to better organize the program by defining a Person class, and then by creating the Mother and Child classes as derived from Person.

Figure 13.4.2: Inheritance.
The 'is-a' relationship. A Mother object 'is a' kind of Person. The Mother class thus inherits from the Person class. Likewise for the Child class.

class Person:
    def __init__(self):
        self.name = ""
        self.birthdate = ""
    # ...

class Child(Person):
    def __init__(self):
        Person.__init__(self)
        self.schoolname = ""
    # ...

class Mother(Person):
    def __init__(self):
        Person.__init__(self)
        self.spousename = ""
        self.children = []
    # ...

Feedback?
participation activity
13.4.1: Is-a vs. has-a relationships.
Indicate whether the relationship of the everyday items is an is-a or has-a relationship. Derived classes and inheritance are related to is-a relationships, not has-a relationships.

1)
Pear / Fruit
2)
House / Door
3)
Dog / Owner
4)
Mug / Cup

Feedback?
challenge activity
13.4.1: Is-a versus has-a relationships.
712910.5105864.qx3zqy7
Start
Indicate the relationship each of the following items have with Vehicle.CarVehicleTruckVehicleVehicleSeatVehicleWheel
Pick

Pick

Pick

Pick
1
2
Check
Next
1
2

Feedback?
How was this section?

|


Provide section feedback'''
##########################Figure 13.4.1: Composition.
"The 'has-a' relationship. A Mother object 'has-a' string object and 'has' child objects, but no inheritance is involved."
class Child:
    def __init__(self):
        self.name = ""
        self.birthdate = ""
        self.schoolname = ""
    # ...

class Mother:
    def __init__(self):
        self.name = ""
        self.birthdate = ""
        self.spouse_name = ""
        self.children = []
    # ...

##########################Figure 13.4.2: Inheritance.
"The 'is-a' relationship. A Mother object 'is a' kind of Person. The Mother class thus inherits from the Person class. Likewise for the Child class."
class Person:
    def __init__(self):
        self.name = ""
        self.birthdate = ""
    # ...

class Child(Person):
    def __init__(self):
        Person.__init__(self)
        self.schoolname = ""
    # ...

class Mother(Person):
    def __init__(self):
        Person.__init__(self)
        self.spousename = ""
        self.children = []
    # ...

##########################
# participation activity
# 13.4.1: Is-a vs. has-a relationships.
# Indicate whether the relationship of the everyday items is an is-a or has-a relationship. Derived classes and inheritance are related to is-a relationships, not has-a relationships.
{
    {
        "Pear / Fruit",
        "is-a"
    },
    {
        "House / Door",
        "has-a"
    },
    {
        "Dog / Owner",
        "has-a"
    },
    {
        "Mug / Cup",
        "is-a"
    }
}
##########################
'''challenge activity

## 

13.4.1: Is-a versus has-a relationships.

712910.5105864.qx3zqy7

 

Start Jump to level 1

Indicate the relationship each of the following items have with Vehicle.

Car

Vehicle

Truck

Vehicle

Vehicle

Seat

Vehicle

Wheel

Pick has-a is-a

Pick has-a is-a

Pick has-a is-a

Pick has-a is-a

1

2

Check

Next

Try again

question\_mark signifies a specific hint for an answer

Show solution

**Done**. Click any level to practice more. Completion is preserved.

✖ ![Correct](https://zytools.zybooks.com/zyBooks2/fingerprinted/e6ed6b01-5dff-40e3-82f5-77f61bbe09cd/utilities/resource/checkmark.png)

Solution

1

2

Feedback?
CarVehicleTruckVehicleVehicleSeatVehicleWheel
'''

{
    "Car / Vehicle": "is-a",
    "Truck / Vehicle": "is-a",
    "Vehicle / Vehicle": "is-a",
    "Seat / Vehicle": "has-a",
    "Wheel / Vehicle": "has-a"
    
}
##########################
'''challenge activity
13.4.1: Is-a versus has-a relationships.
712910.5105864.qx3zqy7
Jump to level 1
Indicate the relationship each of the following items have with Animal.AnimalAnimalCatAnimalBowlCageAnimalOwner
Pick

Pick

Pick

Pick
1
2
Check
Next
1
2

Feedback?
How was this section?

|


Provide section feedback'''
{
    "Animal / Animal": "is-a",
    "Cat / Animal": "is-a",
    "Bowl / Animal": "has-a",
    "Cage / Animal": "has-a",
    "Owner / Animal": "has-a"
}

#A,B
#A,C
#C,A
#A,O
{
    "Animal / Bowl": "has-a",
    "Animal / Cage": "has-a",
    "Cat / Animal": "is-a",
    "Animal / Owner": "has-a",
}
####################################################13.5 Mixin classes and multiple inheritance
'''13.5 Mixin classes and multiple inheritance
A class can inherit from more than one base class, a concept known as multiple inheritance. The derived class inherits all of the class attributes and methods of every base class.

participation activity
13.5.1: Multiple inheritance.


1

2

VampireBat can access methods of WingedAnimal and Mammal.
VampireBatwingspanflap_wings()breathe()give_birth()WingedAnimalwingspanflap_wings()Mammalbreathe()give_birth()WingedAnimalMammalVampire bat
Static figure: WingedAnimal has data member wingspan and method flap_wings(). Mammal has methods breathe() and give_birth(). VampireBat inherits from both WingedAnimal and Mammal, so VampireBat has data member wingspan and methods flap_wings(), breathe(), and give_birth(). Step 1: Vampire bats are both winged animals and mammals. WingedAnimal has data member wingspan and method flap_wings(). Mammal has methods breathe() and give_birth(). Step 2: VampireBat can access methods of WingedAnimal and Mammal. VampireBat has data member wingspan and methods flap_wings(), breathe(), and give_birth().

Captions
Vampire bats are both winged animals and mammals.
VampireBat can access methods of WingedAnimal and Mammal.
Playing step 2: VampireBat can access methods of WingedAnimal and Mammal. Step finished playing

Feedback?
A class can inherit from multiple base classes by specifying multiple items in the inheritance list:

Figure 13.5.1: Inheriting from multiple base classes.
class VampireBat(WingedAnimal, Mammal):  # Inherit from WingedAnimal, Mammal classes
    # ...

Feedback?
A common use of multiple inheritance is extending the functionality of a class using mixins. Mixins are classes that provide some additional behavior, by "mixin in" new methods, but are not meant to be instantiated.

Figure 13.5.2: Using mixins to extend a class's functionality with new methods.
class DrivingMixin:
    def drive(self, distance):
        # ...

    def change_tire(self):
        # ...

    def check_oil(self):
        # ...

class FlyingMixin:
    def fly(self, distance, altitude):
        # ...

    def roll(self):
        # ...

    def eject(self):
        # ...

class TransportMode:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def display(self):
        print(f"{self.name} can go {self.speed} mph")

class SemiTruck(TransportMode, DrivingMixin):
    def __init__(self, name, speed, cargo):
        TransportMode.__init__(self, name, speed)
        self.cargo = cargo

    def go(self, distance):
        self.drive(distance)
        # ...

class FlyingCar(TransportMode, FlyingMixin, DrivingMixin):
    def __init__(self, name, speed, max_altitude):
        TransportMode.__init__(self, name, speed)
        self.max_altitude = max_altitude

    def go(self, distance):
        self.fly(distance / 2, self.max_altitude)
        # ...
        self.drive(distance / 2)

s = SemiTruck("MacTruck", 85, "Frozen beans")
f = FlyingCar("Jetson35K", 325, 15000)

s.go(100)
f.go(100)

Feedback?
Above, the DrivingMixin and FlyingMixin classes each define a set of methods. Any class can be derived from one or both of the mixins. Note that the resolution order by which the base classes are searched for an attribute is related to the order in which classes appear in the inheritance list parentheses. The resolution order is from left to right, so in the FlyingCar class, TransportMode is searched first, then FlyingMixin, and finally DrivingMixin. When using a mixin class, a programmer should be careful to either avoid clashing names, or carefully choose the order of classes in the inheritance list.

participation activity
13.5.2: Mixin classes and multiple inheritance.
Consider the above program and class inheritance tree. Match the new class definitions with methods that would be inherited by instances of that class.

How to use this tool
class Camel(TransportMode):
class Jet(TransportMode, FlyingMixin):
class HoverCraft(DrivingMixin, FlyingMixin, TransportMode):
class Motorcycle(DrivingMixin, TransportMode):
display()
display(), fly(), roll(), eject()
display(), drive(), change_tire(), check_oil()
display(), drive(), fly(), change_tire(), roll(), eject(), check_oil()

Reset

Feedback?
How was this section?

|


Provide section feedback'''
##########################Figure 13.5.1: Inheriting from multiple base classes.
class VampireBat(WingedAnimal, Mammal):  # Inherit from WingedAnimal, Mammal classes
    # ...
    pass
##########################Figure 13.5.2: Using mixins to extend a class's functionality with new methods.
class DrivingMixin:
    def drive(self, distance):
        # ...
        pass

    def change_tire(self):
        # ...
        pass


    def check_oil(self):
        # ...
        pass

class FlyingMixin:
    def fly(self, distance, altitude):
        # ...
        pass  

    def roll(self):
        # ...
        pass

    def eject(self):
        # ...
        pass

class TransportMode:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def display(self):
        print(f"{self.name} can go {self.speed} mph")

class SemiTruck(TransportMode, DrivingMixin):
    def __init__(self, name, speed, cargo):
        TransportMode.__init__(self, name, speed)
        self.cargo = cargo

    def go(self, distance):
        self.drive(distance)
        # ...

class FlyingCar(TransportMode, FlyingMixin, DrivingMixin):
    def __init__(self, name, speed, max_altitude):
        TransportMode.__init__(self, name, speed)
        self.max_altitude = max_altitude

    def go(self, distance):
        self.fly(distance / 2, self.max_altitude)
        # ...
        self.drive(distance / 2)

s = SemiTruck("MacTruck", 85, "Frozen beans")
f = FlyingCar("Jetson35K", 325, 15000)

s.go(100)
f.go(100)
##########################Participation activity
# 13.5.2: Mixin classes and multiple inheritance.
# Consider the above program and class inheritance tree. Match the new class definitions
# with methods that would be inherited by instances of that class.
{
    "class Camel(TransportMode)": "display()",
    "class Jet(TransportMode, FlyingMixin)": "display(), fly(), roll(), eject()",
    "class HoverCraft(DrivingMixin, FlyingMixin, TransportMode)": "display(), drive(), fly(), change_tire(), roll(), eject(), check_oil()",
    "class Motorcycle(DrivingMixin, TransportMode)": "display(), drive(), change_tire(), check_oil()"
}
####################################################13.6 Testing your code The unittest module
'''13.6 Testing your code: The unittest module
A critical part of software development is testing that a program behaves correctly. For large projects, changing code in one file or class may create new bugs in other parts of the program that import or inherit from the changed code. Maintaining a test suite, or a set of repeatable tests, that run after changing the source code of a program is critical.

A programmer commonly performs unit testing, or testing the individual components of a program, such as specific methods, class interfaces, data structures, and so on. The Python standard library unittest module implements unit testing functionality.

Figure 13.6.1: Unit testing with the unittest module.
import unittest

# User-defined class
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def compute_area(self):
        return 3.14 * self.radius**2


# Class to test Circle
class TestCircle(unittest.TestCase):
    def test_compute_area(self):
        c = Circle(0)
        self.assertEqual(c.compute_area(), 0.0)

        c = Circle(5)
        self.assertEqual(c.compute_area(), 78.5)

    def test_will_fail(self):
        c = Circle(5)
        self.assertLess(c.compute_area(), 0)

if __name__ == "__main__":
    unittest.main()
.F
======================================================================
FAIL: test_will_fail (__main__.TestCircle)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "area.py", line 23, in test_will_fail
    self.assertLess(c.compute_area(), 0)
AssertionError: 78.5 not less than 0

----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (failures=1)

Feedback?
The program above implements a unit test for the Circle.compute_area() method. A new class, TestCircle, is defined that inherits from unittest.TestCase. Methods within the TestCircle class that begin with "test_" are the unit tests to be run. A unit test performs assertions to check if a computed value meets certain requirements. Above, self.assertEqual( c.compute_area(), 78.5 ) asserts that the result of c.compute_area() is equal to 78.5. If the assertion is not true, then an AssertionError will be raised and the current test will report as a failure. Executing the unittest.main() function begins the test process. After all tests have completed, a report is automatically printed.

Assertions for many types of relationships exist, for example assertEqual() tests equality, assertIn tests if a value is in a container, etc. The below table (from docs.python.org) lists common assertions.

Table 13.6.1: Assertion methods.
Method	Checks that
assertEqual(a, b)	a == b
assertNotEqual(a,b)	a != b
assertTrue(x)	bool(x) is True
assertFalse(x)	bool(x) is False
assertIs(a, b)	a is b
assertIsNot(a,b)	a is not b
assertIsNone(x)	x is None
assertIsNotNone(x)	x is not None
assertIn(a, b)	a in b
assertNotIn(a, b)	a not in b
assertAlmostEqual(a, b)	round(a - b, 7) == 0
assertGreater(a, b)	a > b
assertGreaterEqual(a, b)	a >= b
assertLess(a, b)	a < b
assertLessEqual(a, b)	a <= b

Feedback?
Try 13.6.1: Writing unit tests.

Full screen
Complete the unit tests for testing the evens() and odds() methods. Each unit test should call either odds() or evens(), passing in a known array of values, and then testing the result to ensure only the correct values are in the array.


Model Solution

Feedback?
participation activity
13.6.1: Unit testing.
1)
What is the Python standard library module that allows the definition of unit tests?

Check

Show answer
2)
Write an assertion that checks if c.valid is True.
def test_a(self):
    c = Widget()
    self.

 

Check

Show answer
3)
Write an assertion that checks if c.sprockets is less than 5.
def test_b(self):
    c = Widget()
    self.

 

Check

Show answer

Feedback?
How was this section?

|


Provide section feedback'''
##########################Figure 13.6.1: Unit testing with the unittest module.
import unittest

# User-defined class
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def compute_area(self):
        return 3.14 * self.radius**2


# Class to test Circle
class TestCircle(unittest.TestCase):
    def test_compute_area(self):
        c = Circle(0)
        self.assertEqual(c.compute_area(), 0.0)

        c = Circle(5)
        self.assertEqual(c.compute_area(), 78.5)

    def test_will_fail(self):
        c = Circle(5)
        self.assertLess(c.compute_area(), 0)

if __name__ == "__main__":
    unittest.main()
##########################Try 13.6.1: Writing unit tests.
#Complete the unit tests for testing the evens() and odds() methods. Each unit test should call either odds() or evens(), passing in a known array of values, and then testing the result to ensure only the correct values are in the array.
import unittest

def evens(numbers):
    """Return the even values in numbers"""
    return [i for i in numbers if (i % 2 == 0)]

def odds(numbers):
    """Return the odd values in numbers"""
    return [i for i in numbers if (i % 2 == 1)]

class TestNumbers(unittest.TestCase):
    test_nums = [1, 3, 5, 6, 8, 2, 1]

    def test_evens(self):
        self.assertEqual(evens(self.test_nums), [6, 8, 2])

    def test_odds(self):
        self.assertEqual(odds(self.test_nums), [1, 3, 5, 1])

if __name__ == "__main__":
    unittest.main()
##########################Participation activity
# 13.6.1: Unit testing.
'''participation activity
13.6.1: Unit testing.
1)
What is the Python standard library module that allows the definition of unit tests?

Check

Show answer
2)
Write an assertion that checks if c.valid is True.
def test_a(self):
    c = Widget()
    self.

 

Check

Show answer
3)
Write an assertion that checks if c.sprockets is less than 5.
def test_b(self):
    c = Widget()
    self.

 

Check

Show answer'''

{
    {
        "What is the Python standard library module that allows the definition of unit tests?",
        "unittest"
    },
    {
        "Write an assertion that checks if c.valid is True.\ndef test_a(self):\n    c = Widget()\n    self.",
        "assertTrue(c.valid)"
    },
    {
        "Write an assertion that checks if c.sprockets is less than 5.\ndef test_b(self):\n    c = Widget()\n    self.",
        "assertLess(c.sprockets, 5)"
    }
}
#?
#unit test
import unittest
# User-defined class
class Widget:
    def __init__(self):
        self.valid = True
        self.sprockets = 3
# Class to test Widget
class TestWidget(unittest.TestCase):
    def test_a(self):
        c = Widget()
        self.assertTrue(c.valid)

    def test_b(self):
        c = Widget()
        self.assertLess(c.sprockets, 5)
if __name__ == "__main__":
    unittest.main()
#?

##########################scratch work
import unittest
class HI():
    def __init__(self):
        self.valid = True
        self.sprockets = 3
class TestHI(unittest.TestCase):
    def test_a(self):
        c = HI()
        self.assertTrue(c.valid)

    def test_b(self):
        c = HI()
        self.assertLess(c.sprockets, 5)
if __name__ == "__main__":
    unittest.main()