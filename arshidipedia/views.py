from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounting.models import Salary, Pay
from django.contrib.auth.models import User


@login_required(login_url='home')
def home(request):
    users = User.objects.all()
    salaries = Salary.objects.all()
    pays = Pay.objects.all()
    # test = [
    #     {
    #         'name': "obeid",
    #         'prices': [12200, 22222]
    #     },
    #     {
    #         'name': 'ali',
    #         'prices': [1, 2, 1, 2]
    #     }
    # ]
    # li = []
    # dic = {}
    # for user in users:
    #     prices = []
    #     for pay in pays:
    #         if pay.payer.id == user.id:
    #             prices.append(pay.price)
    #     dic['username'] = user.username
    #     dic['prices'] = prices
    #     li.append(dic)

    context = {
        'salaries': salaries,
        'pays': pays,
        'users': users,
        # 'li': li,
    }
    return render(request, 'index.html', context)
