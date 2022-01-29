from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounting.models import Salary, Pay, Income
from django.contrib.auth.models import User, Group


@login_required(login_url='/admin')
def home(request):

    income_official_account = Income.objects.income_official_account()
    sum_income_official_account = Income.objects.sum_income_official_account()
    pays = Pay.objects.pay_source_company()

    context = {
        'pays': pays,
        'official_incomes': income_official_account,
        'sum_of_official_incomes': sum_income_official_account,
    }

    return render(request, 'index.html', context)
