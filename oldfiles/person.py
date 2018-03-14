
class Person:

    foo = 'bar'

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def greet(self):
        return 'Hello there'

    @staticmethod   
    def wave():
        #return '*waving hands feverishly*'
        return foo

    @classmethod
    def say_foo(clear):
        return clear.foo