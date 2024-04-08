# Паттерн Адаптер (Adapter) предназначен для преобразования интерфейса одного класса в интерфейс другого. 
# Благодаря реализации данного паттерна мы можем использовать вместе классы с несовместимыми интерфейсами.

# Target: представляет объекты, которые используются клиентом

# Client: использует объекты Target для реализации своих задач

# Adaptee: представляет адаптируемый класс, который мы хотели бы использовать у клиента вместо объектов Target

# Adapter: собственно адаптер, который позволяет работать с объектами Adaptee как с объектами Target.

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

# Строитель (Builder) - шаблон проектирования, который инкапсулирует 
# создание объекта и позволяет разделить его на различные этапы.