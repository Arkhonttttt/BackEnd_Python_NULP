from datetime import date


class Department:
    def __init__(self, department_id, depWorkersNum, depMonthlyBudget):
        self.department_id = department_id
        self.depWorkersNum = depWorkersNum
        self.depMonthlyBudget = depMonthlyBudget
        self.__expenses = 0

    def hire_employee(self):
        self.depWorkersNum += 1
        print(f"Department {self.department_id}: hired a new employee. Total workers: {self.depWorkersNum}")

    def fire_employee(self):
        if self.depWorkersNum > 0:
            self.depWorkersNum -= 1
            print(f"Department {self.department_id}: fired an employee. Total workers: {self.depWorkersNum}")
        else:
            print("No employees to fire!")

    def spend_budget(self, amount):
        if self.depMonthlyBudget - self.__expenses - amount > 0:
            self.__expenses += amount
            print(
                f"Department {self.department_id} spent {amount}. Remaining budget: {self.depMonthlyBudget - self.__expenses}")
        else:
            print("Not enough budget!")

class Position:
    def __init__(self, position_id, posName, posBaseSalary):
        self.position_id = position_id
        self.posName = posName
        self.posBaseSalary = posBaseSalary

    @staticmethod
    def descr():
        print('Our company has the best working conditions for each position')

class Person:
    def __init__(self, name, birth_date, bank_account):
        self.name = name
        self.birth_date = birth_date
        self.__bank_account = bank_account

    def get_bank_account(self):
        return self.__bank_account

    def get_age(self):
        year, month, day = self.birth_date.split('-')
        age = date.today().year - int(year)
        if int(month) < date.today().month:
            return age - 1
        elif int(day) < date.today().day and int(month) < date.today().month:
            return age - 1
        else:
            return age

class WorkEntity:
    def __init__(self, department: Department, position: Position):
        self.department = department
        self.position = position
        self.__salary = self.position.posBaseSalary

    def get_salary(self):
        return self.__salary

    def raise_salary(self, percent):
        self.__salary *= (1 + percent/100)


class Employee(Person, WorkEntity):
    def __init__(self, employee_id, name, birth_date, bank_account, department: Department, position: Position):
        Person.__init__(self, name, birth_date, bank_account)
        WorkEntity.__init__(self, department, position)
        self.employee_id = employee_id

    def object_description(self):
        print(f'Employee {self.name} works in {self.department.department_id} department on a position {self.position.posName}')

    def spend_budget(self, amount):
        print(amount, 'will be spent from department budget by', self.name)
        self.department.spend_budget(amount)

class Payment():
    def __init__(self, employee: Employee):
        self.payment_inf = []
        self.employee = employee

    def create_payment(self):
        self.payment_inf.append(('paid', self.employee.get_salary()))
        self.payment_inf.append(('to employee by id', self.employee.employee_id))
        self.payment_inf.append(('by name', self.employee.name))
        self.payment_inf.append(('Date', date.today()))
        return self.payment_inf

    def get_payment_details(self):
        for data in self.payment_inf:
            a, b = data
            print(a, b)

    def object_description(self):
        print (f'Creates a payment to employee {self.employee.employee_id} and stores data about it')

class CardPayment(Payment):
    def __init__(self, employee: Employee):
        super().__init__(employee)

    def create_payment(self):
        super().create_payment()
        self.payment_inf.append(('to a bank account', self.employee.get_bank_account()))
        return self.payment_inf

class CashPayment(Payment):
    def __init__(self, employee: Employee):
        super().__init__(employee)
        self.payment_inf = []

    def create_payment(self):
        super().create_payment()
        self.payment_inf.append(('in cash', '-'))
        return self.payment_inf


if __name__ == '__main__':
    dep1 = Department(1, 5, 9000)
    dep2 = Department(2, 7, 3000)
    pos1 = Position(1, 'Accountant', 1000)
    emp1 = Employee(1, 'Oleh', '1995-5-5', 1111, dep1, pos1)
    emp2 = Employee(2, 'Andriy', '1989-1-1', 2222, dep2, pos1)

    dep2.spend_budget(100)
    dep1.spend_budget(100)
    dep2.fire_employee()
    emp1.spend_budget(150)
    print('age:', emp2.get_age())
    print('age:', emp1.get_age())
    print('salary:', emp2.get_salary())
    emp1.raise_salary(15)
    print('salary:', emp1.get_salary())
    emp1.object_description()
    payment1 = CardPayment(emp1)
    payment1.create_payment()
    payment1.get_payment_details()
    payment1.object_description()