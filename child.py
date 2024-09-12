class Base:
    def __init__(self, greeting):
        self.greeting = greeting

    @classmethod
    def method(cls, greeting):
        cls.greeting = greeting

    def __str__(self):
        return f'{self.greeting}'


class Child:
    def __init__(self, greeting):
        self.greeting = greeting

    @classmethod
    def method(cls, greeting):
        cls.greeting = greeting

    def __str__(self):
        return f'{self.greeting}'


base1 = Base('Hello from base')
child1 = Child('Hello from child')

print(base1)
print(child1)
