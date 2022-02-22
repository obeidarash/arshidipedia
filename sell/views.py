from django.shortcuts import render, HttpResponse
from .models import Invoice, InvoiceItem
from accounting.models import Income


def invoice(request, invoice_id):
    invoice = Invoice.objects.filter(id=invoice_id).first()
    if not invoice:
        # todo: show 404 page!
        return HttpResponse("Not Found!")
    invoice_item = InvoiceItem.objects.filter(Invoice_id=invoice_id)
    incomes = Income.objects.filter(invoice_id=invoice_id)

    # count sum of invoice price
    invoice_price_count = 0
    for item in invoice_item:
        invoice_price_count += item.quantity * item.price

    # count sum of income price
    income_price_count = 0
    for income in incomes:
        income_price_count += int(income.price)

    context = {
        'invoice': invoice,
        'invoice_item': invoice_item,
        'invoice_price_count': invoice_price_count,
        'income_price_count': income_price_count,
        'incomes': incomes,
    }

    return render(request, 'invoice.html', context)
