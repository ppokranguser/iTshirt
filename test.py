class Parent:
    def __init__(self):
        self.value = 10

    def show_value(self):
        print(self.value)

class Child(Parent):

    def __init__(self):
        super().__init__()
        self.child_value = 20

    #def show_value(self):
    #    print(self.value)

child_instance = Child()

# Parent 클래스의 메서드 호출
child_instance.show_value()
