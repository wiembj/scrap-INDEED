from django.shortcuts import render
from .models import Table

# Create your views here.

def table(request):
    return render(request='table/table.html')