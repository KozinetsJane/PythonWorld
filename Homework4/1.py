class Vehicle:
    def __init__(self, max_speed, mileage):
        self._max_speed = max_speed
        self.__mileage = mileage

    def show_info(self):
        print(f"Max Speed: {self._max_speed}, Mileage: {self.__mileage}")

    def _give_mileage(self):
        return self.__mileage


class Bus(Vehicle):
    def __init__(self, max_speed, mileage, passenger_capacity):
        super().__init__(max_speed, mileage)
        self.passenger_capacity = passenger_capacity 

    def show_info(self):
        mileage = self._give_mileage()
        print(f"Max Speed: {self._max_speed}, Mileage: {mileage}, Passenger Capacity: {self.passenger_capacity}") 


bus1 = Bus(90, 120000, 50)
bus1.show_info()


