import random

class ParentClass1:
    def __init__(self, message, message_id):
        self.message =message
        self.message_id=message_id
    def click_happy(self):
        print("class: ParentClass1, method, click_happy, {}: {}".format(self.message_id, self.message))

    def click_happy_01(self):
        print("class :ParentClass1, method, click_happy_01, {}:{}".format(self.message_id, self.message))

class ChildClass1(ParentClass1):
    def __init__(self, message):
        print("ChildClass1__init__")
        self.message=message
        self.message_id=random.randint(10, 20)
        super().__init__(self.message, self.message_id)

    def click_happy(self):
        print("class: ChildClass1, method, click_happy, {}: {}".format(self.message_id, self.message))

    def click_happy_11(self):
        print("class :ChildClass1, method, click_happy_11, {}:{}".format(self.message_id, self.message))

class ChildClass2(ParentClass1):

    def click_happy(self):
        print("class: ChildClass2, method, click_happy, {}: {}".format(self.message_id, self.message))
    def click_happy_10(self):
        print("class: ChildClass2, method, click_happy_10, {}: {}".format(self.message_id, self.message))

def main():
    print("childClass1 object".center(50, "-"))
    obj1=ChildClass1("checking")
    obj1.click_happy()
    obj1.click_happy_01()
    obj1.click_happy_11()

    print(" ")

    print("ChildClass2 object".center(20, "-"))
    obj2=ChildClass2("checking", 20)
    obj2.click_happy()
    obj2.click_happy_01()
    obj2.click_happy_10()


if __name__=='__main__':
    main()




