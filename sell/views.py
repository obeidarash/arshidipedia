from django.shortcuts import render, HttpResponse
from .models import Invoice, InvoiceItem


def invoice(request, invoice_id):
    invoice = Invoice.objects.filter(id=invoice_id).first()
    if not invoice:
        return HttpResponse("Not Found!")
    invoice_item = InvoiceItem.objects.filter(Invoice_id=invoice_id)
    count = 0
    for item in invoice_item:
        count += item.price
    context = {
        'invoice': invoice,
        'invoice_item': invoice_item,
        'count': count
    }

    return render(request, 'invoice.html', context)
