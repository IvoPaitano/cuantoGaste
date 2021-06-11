from django.db.models import query
from django.db.models.query_utils import Q
from django.shortcuts import redirect, render
from django.http import HttpResponse, response
from . import forms
from django.contrib.auth import authenticate, login, logout
from . import models

app = 'myapp/'

def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    ctx = {
        'data': 'la data en data',
        'data2': 'la data2 en data'
    }
    return render(request, f'{app}home.html', ctx)

def registerUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = forms.CreateUserForm()

    if request.method == 'POST':
        form = forms.CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    ctx = {'form': form}
    return render(request, f'{app}registerUser.html', ctx)

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
    
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

    ctx = {}
    return render(request, f'{app}login.html', ctx)

def logoutUser(request):
    logout(request)
    return redirect('login')


def expenses(request):
    #Verificacion de autenticacion
    if not request.user.is_authenticated:
        return redirect('login')

    #Listado de 'gastos'
    expenses = models.Expense.objects.filter(user = request.user)
    if request.method == 'GET':
        queryset = request.GET.get('buscador')
        if queryset:
            expenses = models.Expense.objects.filter(
                Q(title__icontains = queryset) |
                Q(description__icontains = queryset)
            ).distinct()

    #Formulario para agregar 'gasto'
    form = forms.createExpenseForm()

    if request.method == 'POST':
        form = forms.createExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()

    ctx = {
        'expenses' : expenses,
        'form' : form
    }
    return render(request, f'{app}expense.html', ctx)

def editExpense(request, id):
    #Verificacion de autenticacion
    if not request.user.is_authenticated:
        return redirect('login')
    try:
        expense = models.Expense.objects.filter(user = request.user).get(pk = id)
    except:
        return redirect('expenses')        
    form = forms.EditExpenseForm(instance=expense)


    if request.method == 'POST':
        form = forms.EditExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expenses')
    ctx = {
        'form' : form,
        'title' : 'Editar Gasto'
    }
    
    return render(request, f'{app}editExpense.html', ctx)

def deleteExpense(request, id):
    try:
        expense = models.Expense.objects.filter(user = request.user).get(pk = id)
        expense.delete()
        return redirect('expenses')
    except:
        return redirect('expenses')



