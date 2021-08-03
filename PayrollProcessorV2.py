
from EmployeeTypes import *

class PayrollProcessor:
    def __init__(self, payroll_date):
        self.payroll__date =payroll_date

    def print_payroll_report(self, list_of_employee):
        print("Payroll Report {}".center(50, "-").format(self.payroll__date))
        for emp in list_of_employee:
            if isinstance(emp, Employee):
               print("{}, {}:{:.2f }".format(emp.first_name, emp.last_name, emp.get_monthly_salary()))
            else:
              print("found - the hacker -{} - {} -{:.2f}".format(emp.first_name, emp.last_name, emp.get_monthly_Salary()))

    def print_annual_bonus_report(self, list_employee):
        print("Annual Bonus Report : {}".center(50, "-").format(self.payroll__date))

        for emp in list_employee:
            if isinstance(emp, Employee):
               print("{} {} :{:.2f}".format(emp.first_name, emp.last_name, emp.get_annual_bonus()))
            else:
                print("found - the hacker -{} - {} -{:.2f}".format(emp.first_name, emp.last_name, emp.get_monthly_Salary()))
