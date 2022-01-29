from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounting.models import Salary, Pay, Income
from django.contrib.auth.models import User, Group


@login_required(login_url='/admin')
def home(request):
    users = User.objects.all()
    pays = Pay.objects.pay_source()
    income_official_account = Income.objects.income_official_account()
    sum_income_official_account = Income.objects.sum_income_official_account()

    # returns employee costs based on his pocket
    costs = []
    all_payments_by_user = []
    for user in users:
        for pay in pays:
            # todo : you should add a field to the user model - for example: is_sharik not is_staff
            # is_superuser is equal to is_sharik
            if user.id == pay.payer.id and pay.source == 'employer' and user.is_superuser is True:
                costs.append(int(pay.price))
        payments = {
            'name': user.username,
            'costs': costs,
            'sum': sum(costs)
        }
        all_payments_by_user.append(payments)
        costs = []

        context = {
            'payment': all_payments_by_user,
            'official_incomes': income_official_account,
            'sum_of_official_incomes': sum_income_official_account,
        }

    return render(request, 'index.html', context)
