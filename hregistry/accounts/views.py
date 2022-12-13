from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout ,update_session_auth_hash
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import *
from .forms import *

# Create your views here.
def indexPage(request):
    return redirect(loginPage)

# Create function for user registration
def registerUserPage(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Account was created for ' + username)

    context = {'form': form}
    return render(request, context)

# Create function for user signup
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('records')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('records')

        context = {}
        return render(request, 'accounts/login.html', context)

# Create function for user edit account
def editUserPage(request):
    form = EditUserForm()

    if request.method == "POST":
        form = EditUserForm(request.POST, instnace=request.user)

        if form.is_valid():
            form.save()

        return redirect('index')

    context = {'form': form}
    return redirect(request, context)

# Create function for user remove account
def removeUser(request, pk):
    user = AuthUser.objects.get(pk=pk)
    user.delete()