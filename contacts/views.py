from django.shortcuts import render, Http404
from .models import Company
from django.views.generic import ListView


def company(request, company_id):
    print(company_id)
    return render(request, 'contacts/company.html')
