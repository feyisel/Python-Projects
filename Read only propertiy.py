class Employee():
    __bonus_percentage=0.20
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.__base_annual_salary = 0

        # methods

    def get_monthly_gross(self):
        return self.__base_annual_salary / 12

    def get_standard_annual_bonus_amount(self):
        return self.__base_annual_salary * (self.__bonus_percentage / 100)

    # getter
    @property
    def base_annual_salary(self):
        return self.__base_annual_salary

    @property
    def bonus_percentage(self):
        return self.__bonus_percentage

    # setters
    @base_annual_salary.setter
    def base_annual_salary(self, base_annual_salary):
        if 45000 <= base_annual_salary <= 120000:
            self.__base_annual_salary = base_annual_salary
        else:
            print("Annual base salary must be between 45k and 120k")



def main():
    print("hello from the main() method!")
    employee1 = Employee("feyisal", "jemal")
    employee1.base_annual_salary =50000
    monthly_gross_pay = employee1.get_monthly_gross ()
    standard_annual_bonus = employee1.get_standard_annual_bonus_amount ()
    print("annual salary: {:.2f}".format (employee1.base_annual_salary))
    print("monthly_gross_pay: {:.2f}".format (monthly_gross_pay))
    print("Annual standard bonus:{:.2f}".format (standard_annual_bonus))


if __name__ == '__main__':
    main()
