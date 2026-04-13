class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = EmployeeSalary.get_hours(hours,rest_days)
        self.rest_days = rest_days
        self.email = EmployeeSalary.get_email(name,email)

    def get_hours(hours,rest_days):
        if not hours:
            hours = (7 - rest_days) * 8
        return hours

    def get_email(name,email):
        if not email:
            email = f"{name}@email.com"
        return email

    @classmethod
    def set_hourly_payment(cls, new_payment):
        cls.hourly_payment = new_payment


    def salary(self):
        salary = self.hours * self.hourly_payment
        return salary