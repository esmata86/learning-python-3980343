# LinkedIn Learning Python course by Joe Marini
# Example file for working with classes
#
class Vehicle:
  def __init__(self, body_style):
    self.body_style = body_style
  
  def drive(self, speed):
    self.mode = "driving"
    self.speed = speed

class Car(Vehicle):
  def __init__(self, engine_type):
    super().__init__("Car")
    self.engine = engine_type
    self.wheels = 4
    self.doors = 4

  def drive(self, speed):
    super().drive(speed)
    print(f"Driving my {self.engine} car at {self.speed}")

class Motorcycle(Vehicle):
  def __init__(self, engine_type, has_side_car):
    super().__init__("Motorcycle")
    self.engine = engine_type
    if has_side_car:
      self.wheels = 3
    else:
      self.wheels = 2
    self.doors = 0

  def drive(self, speed):
    super().drive(speed)
    print(f"Driving my {self.engine} moto at {self.speed}")

car1 = Car("gas")
car2 = Car("electric")
mc1 = Motorcycle("gas", True)

print(mc1.wheels)
print(car1.body_style)
print(car2.doors)

car1.drive(30)
car2.drive(40)
mc1.drive(50)