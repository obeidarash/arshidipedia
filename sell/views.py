from django.shortcuts import render


def invoice(request):
    context = {}
    return render(request, 'invoice.html', context)
