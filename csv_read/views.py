from django.shortcuts import render, redirect
from .forms import csv_form


def home(request):
    if request.method == 'POST':
        form = csv_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("Done")
        else:
            context = {'form': form}
            return render(request, "csv_read/home.html", context)
    context = {'form': csv_form}
    return render(request, "csv_read/home.html", context)

