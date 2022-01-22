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
            if user.id == pay.payer.id:
                costs.append(int(pay.price))
        sum_of_costs = sum(costs)
        payments = {
            'name': user.username,
            'costs': costs,
        }
        all_payments_by_user.append(payments)
        costs = []

        context = {
            'payment': all_payments_by_user
        }

    return render(request, 'index.html', context)
