import random


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


def race():
    cars=[]
    for i in range(1,11):
        license_plate=f'ABC-{i}'
        max_speed = random.randint(100,200)
        car = Car(license_plate,max_speed)
        cars.append(car)

    hour=0
    race_ongoing=True

    while race_ongoing:
        hour +=1

        for car in cars:
            speed_change = random.randint(-10,15)
            car.accelerate(speed_change)
            car.drive(1)

            if car.travelled_distance>=10000:
                race_ongoing = False
                break

    print(f"{'license plate':<15}{'maximum speed(km/h)':<20}{'current speed(km/h)':<20}{'travelled distance(km)':<20}")

    for car in cars:
          print(f'{car.license_plate:<15}{car.maximum_speed:<20}{car.current_speed:<20}{car.travelled_distance:<20}')

    def get_distance(final):
        return final.travelled_distance

    winner =max(cars, key=get_distance)
    print(f"\nwinner：{winner.license_plate}, total travelled distance:{winner.travelled_distance}km.")

race()