from django.shortcuts import render

def home(request):
    return render(request, "csv_read/home.html")
