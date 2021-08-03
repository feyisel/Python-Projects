from inhertiance import *
from PayrollProcessor import *


management_employee_1 =Employee("john", "pap", 1010, 5)
salaried_employee_1 =Employee("feyisal", "jemal", 200, 1)
sales_employee_1 = Employee("jack", "toms", 1000, 10)

list_of_employee=[management_employee_1, salaried_employee_1, sales_employee_1]

payroll= PayrollProcessor("07/10/2020")
payroll.print_payroll_report(list_of_employee)
payroll.print_annual_bonus_report(list_of_employee)
