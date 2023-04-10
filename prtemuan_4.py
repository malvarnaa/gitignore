class person:
    def _init_(self, name, age):
        self.name = name
        self.age = age

    def say_my_name(self):
        print("Hallo my name is " + self.name)

    def change_my_name(self, new_name):
        self.name = new_name


class student(person):
    
    def _init_(self, nisn, name, age):
        super()._init_(name, age)
        self.nisn = nisn

    def say_my_name(self):
        print('I am student with name ' + self.name)

person_1 = person("John", 30)
person_1.name = 'emil'
person_1.change_my_name('krishna')
person_1.say_my_name()

student_1 = student('222316', 'fitri', 14)
student_1.say_my_name()

print(person_1.name)
print(person_1.age)
print(person_1.say_my_name())

class mathematic:
    def _init_(self):
        self.value = 0

    def increment(self):
        self.value += 2

    def decrement(self):
        self.value -= 2

    def add(self, a, b):
        return a + b

    def substractions(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b
    
nath_1 = mathematic()
nath_2 = mathematic()

nath_1.increment()
nath_1.increment()
nath_2.decrement()


print(nath_2.value)


print("=======================================================")