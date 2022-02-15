from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounting.models import Salary, Pay, Income
from contacts.models import Contact, Company
from django.contrib.auth.models import User, Group


@login_required(login_url='/admin')
def new_home(request):
    companies = Company.objects.all().order_by('-id')[:5]
    contacts = Contact.objects.all().order_by('-id')[:5]
    pays = Pay.objects.all().order_by('-id')[:5]
    incomes = Income.objects.all().order_by('-id')[:5]
    context = {
        'companies': companies,
        'contacts': contacts,
        'pays': pays,
        'incomes': incomes,
    }
    return render(request, 'index.html', context)


@login_required(login_url='/admin')
def home(request):
    income_official_account = Income.objects.income_official_account()
    sum_income_official_account = Income.objects.sum_income_official_account()
    pay_employer_partner = Pay.objects.pay_employer_partner()
    # pay_employer_worker = Pay.objects.pay_employer_worker()

    context = {
        'pay_employer_partner': pay_employer_partner,
        # 'pay_employer_worker': pay_employer_worker,
        'official_incomes': income_official_account,
        'sum_of_official_incomes': sum_income_official_account,
    }

    return render(request, 'index.html', context)


def search(request):
    companies = []
    if request.method == 'GET':
        query = request.GET.get('q')
        if query == '':
            query = None
        pays = Pay.objects.filter(Q(title__icontains=query))
        companies = Company.objects.filter(Q(name_en__icontains=query) | Q(name_fa__icontains=query))
        contacts = Contact.objects.filter(Q(name_fa__icontains=query) | Q(name_en__icontains=query) |
                                          Q(lastname_en__icontains=query) | Q(lastname_fa__icontains=query))
    print(companies)
    context = {
        'companies': companies,
        'contacts': contacts,
        'pays': pays,
    }
    return render(request, 'search.html', context)
