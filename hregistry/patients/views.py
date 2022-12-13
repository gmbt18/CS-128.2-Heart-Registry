from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout ,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.urls import reverse_lazy,reverse

from datetime import datetime
from django.db.models import F
from .models import *
from .forms import *

from accounts.models import *
from accounts.views import indexPage, loginPage

#redirects to the current year at the start of the page
@login_required(login_url='loginPage')
def indexPage(request):
    year = datetime.now().year
    return redirect(reverse_lazy('records',kwargs={'year':year}))

# Create your views here.

@login_required(login_url='loginPage')
def records(request, year):
    allrecords = Record.objects.all()
    record = Record.objects.filter(date__year = year)
    record_form = RecordForm(request.GET)
    month_today = datetime.now().month
    years = allrecords.annotate(year=F('date__year'))
    months = record.annotate(month=F('date__month'))
    data = {
    'allrecords': allrecords, 
    'records':record, 
    'record_form' : record_form, 
    'years':years, 
    'months' : months, 
    'active_year' : year, 
    'month_today':month_today}
    return render(request, 'patients/records.html', data)
    
# Create function for adding patient
def addRecordPage(request):
    form = RecordForm()

    if request.method == "POST":
        form = RecordForm(request.POST)

        if form.is_valid():
            form.save()

        return redirect('indexPage')
    
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