class Employee():
    __bonus_percentage=0.1
    number_of_Emp =3
    def __init__(self, first_name, last_name, base_annual_salary):
        self.first_name=first_name
        self.last_name=last_name
        self.base_annual_salary =base_annual_salary
        #methods
    def get_monthly_gross(self):
        return self.base_annual_salary/12
    def get_standard_annual_bonus_amount(self):
        return self.base_annual_salary * (self.__bonus_percentage/100)
    def __get_employee_id(self):
        first_name=self.first_name
        return "111-222-444"
    def get_employee(self):
        first_name =self.first_name
        return self.__get_employee_id()

def main():
   print("hello from the main() method!")
   employee1=Employee("feyisal", "jemal", 100000)
   employee1.get_employee()
   empid=employee1.get_employee()
   print("empid : {}".format(empid))
   monthly_gross_pay=employee1.get_monthly_gross()
   standard_annual_bonus =employee1.get_standard_annual_bonus_amount()
   print("annual salary :{:.2f}".format(employee1.base_annual_salary))
   print("Monthly gross salary : {:.2f}".format(monthly_gross_pay))
   print("Annual Standard Bonus: {:.2f}".format(standard_annual_bonus))

   print("class Attributes:".center(50, "-"))
   print("employee1", Employee.number_of_Emp)
if __name__ == '__main__':
        main()
