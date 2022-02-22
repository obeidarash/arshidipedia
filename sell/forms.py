from django import forms
from .models import Invoice


class InvoiceAdminForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = "__all__"

    def check_both_fields(self):
        if self.cleaned_data['company'] == 'null' and self.cleaned_data['contact'] == 'null':
            raise forms.ValidationError('Both cant be empty!')
