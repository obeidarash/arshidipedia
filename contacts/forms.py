from django import forms
from .models import Contact


class ContactAdminForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

    def clean(self):
        if not self.cleaned_data['name_fa'] and not self.cleaned_data['lastname_fa'] and not self.cleaned_data[
            'lastname_en'] and not self.cleaned_data['name_en']:
            raise forms.ValidationError('نام و نام خانوادگی به فارسی یا انگلیسی باید پر شوند')
