# Адаптер - паттерн, позволяющий связать два интерфейса классов, не меняя при этом оригинальные классы

class Dog:
    def __init__(self, name):
        self.name = name  
    def bark(self):
        print("гав")

class Cat:
    def __init__(self, name):
        self.name = name  
    def meow(self):
        print("мяу")

class CatAdapter(Dog):
    def __init__(self, name):
        super(CatAdapter, self).__init__(name)  
        self._cat = Cat(name)  
    def bark(self):
        self._cat.meow()  

dog=CatAdapter("kek")
dog.bark()