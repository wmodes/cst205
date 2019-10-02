class MyClass:
    """A simple example class"""
    i = 12345
    my_string2 = "my_string2"

    def __init__(self, str):
        self.my_string = str

    def hello(self, name):
        print ("hello" + name)
        return 'hello world'

    def give_up_string(self):
        print(self.my_string)

    def test():
        self.hello("Oliver")

x = MyClass("my_string")
print(x)
x.my_string = "my_new_string"
x.my_string2 = "my_new_string2"
print("x.my_string",x.my_string)
print("x.my_string2",x.my_string2)
y = MyClass("my_string")
