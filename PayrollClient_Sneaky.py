
from PayrollProcessorV2 import *
from EmployeeTypes import *
from EmployeeTypes_Hacked import *

management_employee_1 =FullTimeManagementEmployee("john", "pap", 1010, 5)
salaried_employee_1 =FullTimeSalariedEmployee("feyisal", "jemal", 200, 1)
sales_employee_1 = FullTimeSalariedSalesEmployee("jack", "toms", 1000, 10)
sneaky_employee_1 =SneakyEmployee=("sneaky", "sneaky", 1000, 6000)

list_of_employee=[management_employee_1,
                  salaried_employee_1,
                  sales_employee_1,
                  sneaky_employee_1]

payroll= PayrollProcessor("07/10/2020")
payroll.print_payroll_report(list_of_employee)
payroll.print_annual_bonus_report(list_of_employee)
