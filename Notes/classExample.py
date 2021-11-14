
class Employee:
    hike = 1.04
    no_of_employees = 0
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = float(salary)
        self.email = "{}.{}@email.com".format(self.first, self.last)
        Employee.no_of_employees += 1

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None

    def raiseSalary(self):
        self.salary = self.salary * Employee.hike

    @classmethod
    def setHike(cls, hike):
        cls.hike = hike

    @classmethod
    def fromStr(cls, employee_string):
        first, last, sal = employee_string.split("-")
        return cls(first, last, sal)

    @staticmethod
    def isWorkday(day):
        if day.weekday() in [5, 6]:
            return False
        return True

    def __repr__(self):
        return "Employee name {}".format(self.fullname)

    def __str__(self):
        return "Emp {} {} {}".format(self.fullname, self.email, self.salary)

    def __add__(self, other):
        print("adding two salaries...")
        return self.salary + other.salary

    def __len__(self):
        print("length of employee fullname")
        return len(self.fullname)

class Developer(Employee):

    hike = 1.15

    def __init__(self, first, last, salary, program_lang):
        super().__init__(first, last, salary)
        self.program_lang = program_lang

class Manager(Employee):

    def __init__(self, first, last, salary, reporting=None):
        super().__init__(first, last, salary)
        if reporting is None:
            self.reporting = []
        else:
            self.reporting = reporting


    def add_reportee(self, reportee):

        if reportee not in self.reporting:
            self.reporting.append(reportee)


    def remove_reportee(self, reportee):

        if reportee in self.reporting:
            self.reporting.remove(reportee)

    def list_reportees(self):
        for i in self.reporting:
            print("-->", i.fullname)






# Output Test
emp1 = Employee("Raja", "prakash", 120000)
emp2 = Employee("Balaji", "venktesh", 130000)

print(emp1.fullname)
emp1.fullname = "RajaPrakash Muthuraman"
print(emp1)

print(len(emp2))
print(emp1 + emp2)

 # Before and after hike
print(Employee.hike)
Employee.setHike(1.15)
print(Employee.hike)

# From String
empStr3 = "Hari-Krish-55000"
empStr4 = "Prashant-Bala-55000"

emp3 = Employee.fromStr(empStr3)
emp4 = Employee.fromStr(empStr4)

print(emp3.fullname)
print(emp4.__dict__)
print(emp4.raiseSalary())
print(emp4.__dict__)

print("Total No of Employees : ", Employee.no_of_employees)

# Static method test Nothing to do with Class and Self objects

import datetime

myday = datetime.date(1991, 12, 31)

print(Employee.isWorkday(myday))


# Inheritance Test


dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(mgr_1.email)

mgr_1.add_reportee(dev_2)
mgr_1.remove_reportee(dev_2)

mgr_1.list_reportees()