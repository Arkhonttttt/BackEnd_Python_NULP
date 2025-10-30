# Файл: repository_app/management/commands/demo_repo.py

from django.core.management.base import BaseCommand

from repository_app.repository import PositionRepo, DepartmentRepo, EmployeeRepo

class Command(BaseCommand):
    help = 'Запускає демонстрацію роботи репозиторіїв'

    def handle(self, *args, **options):
        position = PositionRepo()
        department = DepartmentRepo()
        employee = EmployeeRepo()

        print('get_all() for Position: ')
        positons = position.get_all()
        for pos in positons:
            print('  ID:', pos.position_id, 'Назва:', pos.position_name)

        print('create() for Department: ')
        new_dep_data = {
            'number_of_workers': '1',
            'monthly_budget': 1337,
            'department_chief_id': 8,
        }

        new_dep = department.create(new_dep_data)

        print('get_by_id() for Employee: ')
        empl = employee.get_by_id(3)
        print(empl.first_name, empl.last_name, empl.email)
