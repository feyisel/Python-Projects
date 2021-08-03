
class SneakyEmployee:
    def __init__(self, first_name, last_name, emp_id , years_experience, annual_salary):
        self.first_name=first_name
        self.last_name=last_name
        self.emp_id =emp_id
        self.years_experience=years_experience
        self.annual_salary=annual_salary

    def get_monthly_salary(self):
        return round(self.annual_salary / 12, 2)

    def get_annual_bonus(self):
        return round(self.annual_salary/2, 2)