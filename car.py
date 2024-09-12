class Car:
    def __init__(self, name: str, model: str, year: int, speed: int):
        self.name = name
        self.__model = model
        self.year = year
        self.__speed = speed

    def set_model(self, model):
        if len(model) > 8:
            print('Model name must be < 8 characters')
        else:
            self.__model = model

    def set_speed(self, speed):
        if speed >= 400:
            print('Motor car must be less than 400 km/h')
        else:
            self.__speed = speed

    def get_model(self):
        return self.__model

    def get_speed(self):
        return self.__speed

    def __str__(self):
        return (f'Name of car: {self.name}, year of manufaturing: {self.year}. Model: {self.__model},'
                f' and speed of this model: {self.__speed}')


car1 = Car('Mazda', 'Miata', 2012, 320)
print(car1)

car1.set_model('dfkfkfkfkfkfkf') #Error
car1.set_model('Capella')
car1.set_speed(240)
print(car1)
car1.set_speed(600) #Error

