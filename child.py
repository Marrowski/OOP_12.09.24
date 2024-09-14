class Base:
    @classmethod
    def method(cls):
        print('Hello from Base')


class Child:
    @classmethod
    def method(cls):
        print('Hello from Child')


Base.method()
Child.method()
