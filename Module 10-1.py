#Module 10-1

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


        print(f"\nMoving from floor {self.current_floor} to floor {target}:")

        if target > self.current_floor:
            while self.current_floor < target:
                self.floor_up()
            return

        else:
            while self.current_floor > target:
                self.floor_down()
            return


#main program
h = Elevator(1, 10)
print("Basic elevator test:")
h.go_to_floor(5)
h.go_to_floor(1)


