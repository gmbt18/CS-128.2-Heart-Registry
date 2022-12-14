from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout ,update_session_auth_hash
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy,reverse
from django.contrib.auth.forms import PasswordChangeForm

from bootstrap_modal_forms.generic import BSModalDeleteView

from .models import *
from .forms import *
from datetime import datetime
from patients.models import Staff

# Create your views here.
def indexPage(request):
    return redirect(loginPage)

# Create function for user registration
def registerUserPage(request):
    form = CreateUserForm()
    ut=0
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            user = form.save(False)
            user.user_type=ut
            user.save()

            username = form.cleaned_data.get('username')
            if ut == 2:
                Staff.objects.create(user=user, first_name=user.first_name, last_name=user.last_name, title='Dr.')
            else:
                Staff.objects.create(user=user, first_name=user.first_name, last_name=user.last_name)

            messages.success(request, 'Account was created for ' + username)
        
            return redirect('manageUsers')

    context = {'form': form}
    return render(request, context)

# Create function for user signup
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('indexPage')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('indexPage')

        context = {}
        return render(request, 'accounts/login.html', context)

def logOutPage(request):
    logout(request)
    return redirect('loginPage')


@login_required(login_url='loginPage')
def viewProfile(request):
    user = request.user
    context = {'user':user}
    return render(request,'accounts/profile.html', context)

@user_passes_test(lambda u : u.is_superuser)
@login_required(login_url='loginPage')
def manageUsers(request):
    users = AuthUser.objects.exclude(user_type=None)
    
   
    if request.method =="POST" and request.POST.get('role'):
        role = request.POST.get('role')
        if role == 'nurse':
            users = AuthUser.objects.filter(user_type=1)
            
        elif role == 'doctor':
            
            users = AuthUser.objects.filter(user_type=2)
            
        elif role == 'radtech':
            users = AuthUser.objects.filter(user_type=3)
            
        elif role == 'medtech':
            users = AuthUser.objects.filter(user_type=4)
               
   
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            user = form.save(False)
            user.save()

            username = form.cleaned_data.get('username')
            if user.user_type == 2:
                Staff.objects.create(user=user, first_name=user.first_name, last_name=user.last_name, title='Dr.')
            else:
                Staff.objects.create(user=user, first_name=user.first_name, last_name=user.last_name)

            messages.success(request, 'Account was created for ' + username)
        
            return redirect('manageUsers')
    context={'form':form,'users':users}
    return render(request,"accounts/users.html",context)

def editProfile(request):
    user = request.user
    form = EditUserForm(instance=user)

    if request.method == "POST":
        form = EditUserForm(request.POST, instance=user)

        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse_lazy('viewProfile'))

    context={'form':form}
    return render(request,'accounts/edit-user.html',context)

def users(request):
    data = dict()
    if request.method == 'GET':
        users = AuthUser.objects.exclude(username='admin')
        data['table'] = render_to_string(
            'accounts/user-table.html',
            {'users': users},
            request=request
        )
        return JsonResponse(data)

#edit user modal
def editUser(request,pk):
    user = AuthUser.objects.get(id=pk)
    if request.method == "POST":
        form= EditUserForm(request.POST, instance=user)

        if form.is_valid():
            form.save()
            
        return HttpResponseRedirect(reverse_lazy('manageUsers'))

    else:
        form = EditUserForm(instance=user)

        context = {'form': form,'u':user}
        return render(request, 'accounts/edit-user.html', context)
#change user password
def changePass(request,pk):
    user = AuthUser.objects.get(id=pk)
    pw = PasswordChangeForm(user)
    if request.method == "POST":
        pw = PasswordChangeForm(data=request.POST, user=user)
        if pw.is_valid():
            pw.save()
            update_session_auth_hash(request, pw.user)
    context = {'pw': pw}
    return render(request, 'accounts/change-password.html', context)

#change password for admin
def changeAdminPass(request):
    user = request.user
    pw = PasswordChangeForm(user)
    if request.method == "POST":
        pw = PasswordChangeForm(data=request.POST, user=user)
        if pw.is_valid():
            pw.save()
            update_session_auth_hash(request, pw.user)
    context = {'pw': pw}
    return render(request, 'accounts/change-password.html', context)

#delete user modal
class deleteUser(BSModalDeleteView):
    model = AuthUser
    template_name = 'accounts/delete-user.html'
    success_message = 'Success: User was deleted.'
    success_url = reverse_lazy('manageUsers')