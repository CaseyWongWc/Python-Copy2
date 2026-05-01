class Vehicle:
  def __init__(self):
      self.speed = 0

  def set_speed(self, speed_to_set):
      self.speed = speed_to_set

  def print_speed(self):
      print(self.speed)
      # out: 55


class Car(Vehicle):
  def print_car_speed(self):
      print("Speed: ", end = "")
      # out: Speed: 
      self.print_speed()
      # val: None


myCar = Car()
myCar.set_speed(55)
# val: None
myCar.print_car_speed()
# val: None