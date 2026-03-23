#Module 10-2
class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f'Elevator moved up to floor {self.current_floor}.')
            return

        else:
            print(f"Already at the top floor {self.top_floor}")
            return

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f'Elevator moved down to floor {self.current_floor}.')
            return

        else:
            print(f"Already at the bottom floor {self.bottom_floor}")
            return


    def go_to_floor(self,target):
        if target == self.current_floor:
            print(f'We are arriving at floor {target}.')
            return

        print(f"\nMoving from floor {self.current_floor} to floor {target}:")

        if target > self.current_floor:
            while self.current_floor < target:
                self.floor_up()
            return

        else:
            while self.current_floor > target:
                self.floor_down()
            return

class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor =bottom_floor
        self.top_floor =top_floor
        self.num_elevators =num_elevators
        self.elevators=[]

        for i in range(num_elevators):
            elevator= Elevator(bottom_floor,top_floor)
            self.elevators.append(elevator)

        print(f"Floors {bottom_floor} to {top_floor},{num_elevators} elevators")

    def run_elevator(self,elevator_number,destination_floor):

        elevator = self.elevators[elevator_number]

        print(f"Running Elevator {elevator_number} to floor {destination_floor}")
        elevator.go_to_floor(destination_floor)



#main program
# Test Building with multiple elevators
building = Building(1, 10, 3)
building.run_elevator(0, 5)
building.run_elevator(1, 3)
building.run_elevator(2, 8)

# Test single elevator building
small_building = Building(0, 5, 1)
small_building.run_elevator(0, 4)

# Test larger building
office = Building(1, 6, 5)
office.run_elevator(0, 4)
office.run_elevator(4, 2)





