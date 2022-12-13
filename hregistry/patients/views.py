from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout ,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import *
from .forms import *

from accounts.models import *

# Create your views here.
def records(request):
    record = Record.objects.all()
    data = {'records':record}
    return render(request, 'patients/records.html', data)
# Create function for adding patient
def addRecordPage(request):
    form = RecordForm()

    if request.method == "POST":
        form = RecordForm(request.POST)

        if form.is_valid():
            form.save()

        return redirect('index')
    
    context = {'form': form}
    return render(request, context)

# Create function for removing patient
def removeRecord(request, id):
    record = Record.objects.get(id=id)
    record.delete()

# Create function for editing patient details
def editRecordPage(request, id):
    record = Record.objects.get(id=id)
    form = EditRecordForm(instance=record)

    if request.method == "POST":
        form = EditRecordForm(request.POST, instance=record)

        if form.is_valid():
            form.save()
            return redirect("index", id=record.id)

    context = {'record': record, 'form': form}
    return render(request, context)

# Create function for adding staff
def addStaffPage(request):
    form = StaffForm()

    if request.method == "POST":
        form = StaffForm(request.POST)

        if form.is_valid():
            staff = form.save(False)
            staff.first_name = request.POST['first_name']
            staff.last_name = request.POST['last_name']
            staff.save()

        return redirect("index")
    
    context = {'form': form}
    return render(request, context)

# Create function for patient search

# Create function for patient filter

# Create function for pdf export