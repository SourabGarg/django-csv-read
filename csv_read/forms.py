from django import forms
from .models import CSVUpload


class csv_form(forms.ModelForm):
    class Meta:
        model = CSVUpload
        fields = ['csv']
        widgets = {
            'csv': forms.FileInput(attrs={'accept': '.svg, .csv'})
        }
