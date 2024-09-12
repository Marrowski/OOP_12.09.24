class Temperature:
    def __init__(self, temperature):
        self.temperature = temperature

    def fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print('Input a temperature')
        return self._temperature

    @temperature.setter
    def temperature(self, val):
        print('Lets set value')
        if val < -273.15:
            print('Temperature under -273.15 is impossible')
        else:
            self._temperature = val


temperature = Temperature(5)
print(temperature.temperature)
print(temperature.fahrenheit())
