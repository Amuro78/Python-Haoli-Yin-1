class Car:

    def __init__(
            self, license_plate, maximum_speed
    ):
        self.license_plate=license_plate
        self.maximum_speed=maximum_speed
        self.current_speed=0
        self.travelled_distance=0

    def accelerate(self,speed):
        self.current_speed += speed
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed

        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self,time):
        self.travelled_distance += time*self.current_speed

car1 = Car("ABC-123", 142)
print(f"Initial distance: {car1.travelled_distance} km")
car1.current_speed= 60
car1.drive(1.5)
print(f"Distance after driving 1.5 hours at 60 km/h: {car1.travelled_distance} km")