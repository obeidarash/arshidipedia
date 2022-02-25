from .models import Income, OfficialInvoices
from django import forms


class OfficialInvoicesAdminForm(forms.ModelForm):
    class Meta:
        model = OfficialInvoices
        fields = "__all__"

    def clean(self):
        if not self.cleaned_data['contact'] and not self.cleaned_data['company']:
            raise forms.ValidationError('مخاطب و شرکت نمیتوانند همزمان خالی باشند')
        elif self.cleaned_data['contact'] and self.cleaned_data['company']:
            raise forms.ValidationError('مخاطب و شرکت نمیتوانند همزمان پر باشند')


class IncomeAdminForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = "__all__"

    def clean(self):
        if not self.cleaned_data['contact'] and not self.cleaned_data['company']:
            raise forms.ValidationError('مخاطب و شرکت نمیتوانند همزمان خالی باشند')
        elif self.cleaned_data['contact'] and self.cleaned_data['company']:
            raise forms.ValidationError('مخاطب و شرکت نمیتوانند همزمان پر باشند')
