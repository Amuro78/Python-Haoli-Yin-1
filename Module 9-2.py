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



car1 = Car("ABC-123", 142)
car1.accelerate(30)
car1.accelerate(70)
car1.accelerate(50)
print(f"Current speed: {car1.current_speed} km/h")
car1.accelerate(-200)
print(f"Current speed: {car1.current_speed} km/h")





