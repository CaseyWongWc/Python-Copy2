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
        "True"
    },
    {
        "When adding a new derived class, a programmer has to change the base class as well.",
        "False"
    }
}