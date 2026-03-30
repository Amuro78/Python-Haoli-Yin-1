import random

import race


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

    def drive(self,hour):
        self.travelled_distance += self.current_speed * hour



class Race:

    def __init__(self, name, distance, car_list):
        self.name = name
        self.distance = distance
        self.cars = car_list
        self.hours_passes = 0

    def hour_passes(self):

        self.hours_passes += 1

        for car in self.cars:
            speed_change = random.randint(-10, 15)

            car.accelerate(speed_change)

            car.drive(1)

    def print_status(self):
        print(f"{'License Plate':<15} {'Max Speed':<12} {'Current Speed':<15} {'Distance':<15} {'Progress':<10}")

        for car in self.cars:
            progress = (car.travelled_distance / self.distance) * 100

            print(f"{car.license_plate:<15} "
                  f"{car.maximum_speed:<12} "
                  f"{car.current_speed:<15} "
                  f"{car.travelled_distance:<15.1f} "
                  f"{progress:<10.1f}%")


    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False

    def get_winner(self):
        if not self.cars:
            return None

        winner = max(self.cars, key=lambda car: car.travelled_distance)
        return winner


cars = []
for i in range(1,11):
    car = Car(f"ABC-{i}", random.randint(100, 200))
    cars.append(car)



race = Race("Grand Demolition Derby", 8000, cars)
race.print_status()
print(f"Race created: {race.name} ({race.distance} km)")
print(f"Cars participating: {len(race.cars)}")

print(f"\nRace finished initially: {race.race_finished()}")

hour=0
while not race.race_finished():
    race.hour_passes()
    hour += 1
    if hour % 10 ==0:
        race.print_status()
