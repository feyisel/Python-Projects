class Car:
    #class Attribute / variables
    number_of_tries =4
    def __init__(self):
        #object attributes
        self.make=""
        self.model =""
        self.year=""
        self.color=""
        self.moon_roof=""
        self.engine_running=False
    #methods
    def start_the_engine(self):
        self.engine_running = True

    def stop_the_engine(self):
        self.engine_running = False

def main():
    print("hello from the main() method!")
    car1 =Car()
    car2 =Car()
    #values
    car1.make="Tesla"
    car1.model="model 3"
    car1.year=2020
    car1.color="blue"
    car1.moon_roof=True
    car2.make="opel"
    car2.model="model 2"
    car2.year=2021
    car2.color="black"
    car2.moon_roof=True
    #Accessing car1 attributes
    print("Printing car1 details:".center(50, "-"))
    print("make : {}".format(car1.make))
    print("model: {} ".format(car1.model))
    print("year: {}".format(car1.year))
    print("color: {}".format(car1.color))
    print("moon Roof: {}".format(car1.moon_roof))
    #Accessing Car2 attributes(object attributes)
    print("Printing car2 details:".center(50, "-"))
    print("make : {}".format(car2.make))
    print("model: {} ".format(car2.model))
    print("year: {}".format(car2.year))
    print("color: {}".format(car2.color))
    print("moon Roof: {}".format(car2.moon_roof))
    #class Attributes
    print("class Attributes:".center(50, "-"))
    print("Car", Car.number_of_tries)
    Car.number_of_tries =23
    print("car1", car1.number_of_tries)
    print("car2", car2.number_of_tries)


if __name__ == '__main__':
        main()
