from .models import AccuralType, OtherAccurals, Bonus, Department, Position, Employee, Payment, Wage, PaymentType

class BaseRepo():
    def get_all(self): pass
    def get_by_id(self, id): pass
    def create(self, name): pass

class AccuralTypeRepo(BaseRepo):
    def get_all(self):
        return AccuralType.objects.all()

    def get_by_id(self, id):
        try:
            return AccuralType.objects.get(id=id)
        except AccuralType.DoesNotExist:
            return None

    def create(self, data: dict):
        return AccuralType.objects.create(**data)

class DepartmentRepo(BaseRepo):
    def get_all(self):
        return Department.objects.all()

    def get_by_id(self, id):
        try:
            return Department.objects.get(department_id=id)
        except Department.DoesNotExist:
            return None

    def create(self, data: dict):
        return Department.objects.create(**data)

class PositionRepo(BaseRepo):
    def get_all(self):
        return Position.objects.all()

    def get_by_id(self, id):
        try:
            return Position.objects.get(position_id=id)
        except Position.DoesNotExist:
            return None

    def create(self, data: dict):
        return Position.objects.create(**data)

class EmployeeRepo(BaseRepo):
    def get_all(self):
        return Employee.objects.all()

    def get_by_id(self, id):
        try:
            return Employee.objects.get(employee_id=id)
        except Employee.DoesNotExist:
            return None

    def create(self, data: dict):
        return Employee.objects.create(**data)

class WageRepo(BaseRepo):
    def get_all(self):
        return Wage.objects.all()

    def get_by_id(self, id):
        try:
            return Wage.objects.get(employee_id=id)
        except Wage.DoesNotExist:
            return None

    def create(self, data: dict):
        return Wage.objects.create(**data)

class PaymentRepo(BaseRepo):
    def get_all(self):
        return Payment.objects.all()

    def get_by_id(self, id):
        try:
            return Payment.objects.get(payment_id=id)
        except Payment.DoesNotExist:
            return None

    def create(self, data: dict):
        return Payment.objects.create(**data)

class PaymentTypeRepo(BaseRepo):
    def get_all(self):
        return PaymentType.objects.all()

    def get_by_id(self, id):
        try:
            return PaymentType.objects.get(payment_type_id=id)
        except PaymentType.DoesNotExist:
            return None

    def create(self, data: dict):
        return PaymentType.objects.create(**data)

class OtherAccuralRepo(BaseRepo):
    def get_all(self):
        return OtherAccurals.objects.all()

    def get_by_id(self, id):
        try:
            return OtherAccurals.objects.get(employee_id=id)
        except OtherAccurals.DoesNotExist:
            return None

    def create(self, data: dict):
        return OtherAccurals.objects.create(**data)


class BonusRepo(BaseRepo):
    def get_all(self):
        return Bonus.objects.all()

    def get_by_id(self, id):
        try:
            return Bonus.objects.get(id=id)
        except Bonus.DoesNotExist:
            return None

    def create(self, data: dict):
        return Bonus.objects.create(**data)

