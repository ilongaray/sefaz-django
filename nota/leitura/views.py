import subprocess

from django.shortcuts import render

# Create your views here.

def index (request):
    subprocess.run(['python', 'leitura/leitura.py'])
    return render(request, 'index.html')