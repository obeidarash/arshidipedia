from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounting.models import Salary, Pay
from django.contrib.auth.models import User


@login_required(login_url='/admin')
def home(request):
    return render(request, 'index.html')
