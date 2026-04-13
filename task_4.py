class EmployeeSalary:

    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = EmployeeSalary.get_hours(hours,rest_days)
        self.rest_days = rest_days
        self.email = EmployeeSalary.get_email(name,email)
        self.hourly_payment = 400

    @classmethod
    def get_hours(cls,hours,rest_days):
        if not hours:
            hours = (7 - rest_days) * 8
        return hours

    @classmethod
    def get_email(cls,name,email):
        if not email:
            email = f"{name}@email.com"
        return email

    def set_hourly_payment(self, hourly_payment):
        self.hourly_payment = hourly_payment

    def salary(self):
        salary = self.hours * self.hourly_payment
        return salary