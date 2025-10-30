from django.shortcuts import render

from .repository import EmployeeRepo, PaymentRepo


def employee_list_view(request):
    employee_repo = EmployeeRepo()
    employees = employee_repo.get_all()
    context = {
        'employees': employees,
    }

    return render(request, 'repository_app/employee_list.html', context)

def get_payment_view(request, id):
    payment_repo = PaymentRepo()

    payment = payment_repo.get_by_id(id)
    context = {
        'payment': payment,
    }