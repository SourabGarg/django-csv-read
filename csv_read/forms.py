from django import forms
from .models import CSVUpload


class csv_form(forms.ModelForm):
    class Meta:
        model = CSVUpload
        fields = ['csv']
        widgets = {
            'csv': forms.FileInput(attrs={'accept': '.csv'})
        }


def delete_all_csv_files():
    for csv_upload in CSVUpload.objects.all():
        csv_upload.csv.delete()
        csv_upload.delete()