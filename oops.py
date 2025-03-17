class Parking:
    def __init__(self, total_spaces):
        self.total_spaces = total_spaces
        self.spaces = [None] * total_spaces

    def park(self, car):
        for i in range(self.total_spaces):
            if self.spaces[i] is None:
                self.spaces[i] = car
                print(f"Car {car} parked in space {i + 1}.")
                return
        print("Parking lot is full.")

    def check_availability(self):
        if None in self.spaces:
            print("Space is available.")
        else:
            print("Parking lot is full.")

    def check_spaces(self):
        available = []
        for i in range(len(self.spaces)):
            if self.spaces[i]== None:
                available.append(i + 1)
        if available:
            print(f"Available spaces: {available}")
        else:
            print(" no spaces available.")

    def remove_car(self,car):
        for i in  range(len(self.spaces)):
            if self.spaces[i] == car:
                self.spaces[i] =  None
                print(f"car is removed successfully :{car}")




parking_lot = Parking(5)
parking_lot.park("bmw")
parking_lot.park("verna")
parking_lot.check_spaces()
parking_lot.check_availability()
parking_lot.remove_car("bmw")
parking_lot.check_spaces()

