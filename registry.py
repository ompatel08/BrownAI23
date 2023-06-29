
class person:
    def __init__ (self, name, age, subject):
        self.name = name
        self.age = age
        self.subject = subject


    def myfunc(self):
        print(self.name + " is " + str(self.age) + " and enrolled in " + self.subject)

p1 = person("John", 36, "math")
p1.myfunc()

