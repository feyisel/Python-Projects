class Car: 
    #class Attribute / variables
    number_of_tries =4
    def __init__(self, make, model, year, color,  moon_year=False):
        #object attributes
        self.make=make
        self.model =model
        self.year=year
        self.color=color
        self.moon_roof=moon_year
        self.engine_running=False
    #methods
    def start_the_engine(self):
        self.engine_running = True

    def stop_the_engine(self):
        self.engine_running = False
        #destructor
    def __del__(self):
        print("{} {}: destructor invoked".format(self.make, self.model))



def main():
    print("hello from the main() method!")
    car1 =Car("ford", "mustang", 2020, "blue")
    car2 =Car("Tesla", "model 3", 2021, "red")

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
    print("Printing car1 details:".center(50, "-"))
    print("class Attributes")
    print("car1", car1.number_of_tries)
    print("car2", car2.number_of_tries)
    print("Car", Car.number_of_tries)
    #delete
    print("deleting object".center(50, "-"))
    del car2
    del car1

if __name__ == '__main__':
        main()

