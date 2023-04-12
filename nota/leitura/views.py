import subprocess

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index (request):
    #resultado = subprocess.check_output(['python', 'leitura/script.py'])
    return render(request, 'index.html')

#def executar_script(request):
#    # Coloque o código do script.py aqui
#    run_script = subprocess.check_output(['python', 'leitura/script.py'])
#    resultado = "O script foi executado com sucesso!"
#    return HttpResponse(run_script, resultado)