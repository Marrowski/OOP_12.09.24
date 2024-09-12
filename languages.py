class English:
    def __init__(self, say_hello: str):
        self.say_hello = say_hello

    def greeting(self, say_hello):
        self.say_hello = say_hello

    def __str__(self):
        return f'Hello in English: {self.say_hello}\n'


class Spanish:
    def __init__(self, say_hola: str):
        self.say_hola = say_hola

    def greeting(self, say_hola):
        self.say_hola = say_hola

    def __str__(self):
        return f'Hello in Spanish: {self.say_hola}'


english = English('Hello')
spanish = Spanish('Hola')


def hello_friend(english, spanish):
    print(english, spanish)


hello_friend(english, spanish)