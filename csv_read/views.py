from django.shortcuts import render, redirect
from .forms import csv_form, delete_all_csv_files


def home(request):
    if request.method == 'POST':
        delete_all_csv_files()
        form = csv_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('result')
        else:
            context = {'form': form}
            return render(request, "csv_read/home.html", context)
    context = {'form': csv_form}
    return render(request, "csv_read/home.html", context)

