from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounting.models import Salary, Pay
from django.contrib.auth.models import User


@login_required(login_url='/admin')
def home(request):
    users = User.objects.all()
    pays = Pay.objects.filter(source='company')
    test = [
        {
            'name': "obeid",
            'prices': [12200, 22222]
        },
        {
            'name': 'ali',
            'prices': [1, 2, 1, 2]
        }
    ]
    payment = {}
    costs = []

    al = []
    for user in users:
        for pay in pays:
            if pay.payer.id == user.id:
                costs.append(pay.price)
        username = user.username
        payment['name'] = username
        payment['costs'] = costs
        al.append(payment)

        context = {
            'payment': al
        }
    return render(request, 'index.html', context)
