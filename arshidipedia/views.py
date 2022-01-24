from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounting.models import Salary, Pay
from django.contrib.auth.models import User


@login_required(login_url='/admin')
def home(request):
    users = User.objects.all()
    pays = Pay.objects.filter(source='employer')

    # returns employee costs based on his pocket
    costs = []
    all_payments_by_user = []
    for user in users:
        for pay in pays:
            # todo : you should add a field to the user model - for example: is_sharik not is_staff
            if user.id == pay.payer.id and user.is_staff is True:
                costs.append(int(pay.price))
        payments = {
            'name': user.username,
            'costs': costs,
            'sum': sum(costs)
        }
        all_payments_by_user.append(payments)
        costs = []

        context = {
            'payment': all_payments_by_user
        }

    return render(request, 'index.html', context)
