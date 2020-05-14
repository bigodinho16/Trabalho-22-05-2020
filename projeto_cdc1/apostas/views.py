from django.shortcuts import render

def index(request):
    return render(request, 'apostas/pag_inicial.html')

def login(request):
    return render(request, 'apostas/login.html')

def cadastro(request):
    return render(request, 'apostas/cadastrar.html')

