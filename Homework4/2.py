class Temperature:
    def __init__(self, celsius):
        self._celsius = None
        self.celsius = celsius 

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Температура не может быть ниже -273.15°C (абсолютный ноль).")
        self.__celsius = value

    @property
    def fahrenheit(self):
        return self.__celsius * 9 / 5 + 32


temp = Temperature(25)
print(temp.fahrenheit) 
