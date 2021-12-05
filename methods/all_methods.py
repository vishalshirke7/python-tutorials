# Key Takeaways
# Instance methods need a class instance and can access the instance through self.
# Class methods don’t need a class instance. They can’t access the instance (self) but they have access to the class itself via cls.
# Static methods don’t have access to cls or self. They work like regular functions but belong to the class’s namespace.
# Static and class methods communicate and (to a certain degree) enforce developer intent about class design. This can have maintenance benefits.


class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'


obj = MyClass()
print(obj.method())
print(obj.classmethod())
print(obj.staticmethod())

print(MyClass.method(obj))
print(MyClass.classmethod())
print(MyClass.staticmethod())