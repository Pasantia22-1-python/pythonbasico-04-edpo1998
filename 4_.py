class Person:
    def __init__(self,name,age):
        self._name = name
        self._age = age

    def say_hello(self):
        print('Hello, my name is {} and I am {} years old.'.format(self._name,self._age))




if __name__ == '__main__':
    person = Person("Erick","23")

    print('Age: {}'.format(person._age))
    person.say_hello()
