class English:
    def greeting(self):
        print('Hello!')


class Spanish:
    def greeting(self):
        print('Hola!')


greeting1 = English()
greeting2 = Spanish()


def hello_friend():
    greeting1.greeting(), greeting2.greeting()


hello_friend()