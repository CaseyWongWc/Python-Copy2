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
'''activity
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
Quantity: 250, Price: $85.00
'''