class Vehicle:
  def __init__(self):
    self.medium = "terrestrial"
    self.engine = None

class Bus(Vehicle):
  def __init__(self):
    Vehicle.__init__(self)
    self.num_wheels = 6
    self.fuel_type = "diesel"

class Engine:
  def __init__(self):
    self.fuel_type = "gas"
    self.num_cylinders = 8
