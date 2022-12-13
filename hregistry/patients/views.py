from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout ,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import *
from .forms import *

from accounts.models import *

import csv

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

# csv export
def exportToCSV(request):
    records = Record.objects.all()
    response = HttpResponse()
    response['Content-Disposition'] = 'attachment; filename=records.csv'
    writer = csv.writer(response)
    writer.writerow(['DATE', 'HOSPITAL', 'FIRST NAME', 'LAST NAME', 'MIDDLE INITIAL', 'AGE', 'SEX', 'UNIT BEFORE', 'CATEGORY', 'IS EMERGENCY', 'SWAB', 'PATHWAY', 'SCHEDULE TIME FROM', 'SCHEDULE TIME TO', 'RECEIVED', 'STARTED', 'ER DOOR', 'ACTI', 'WIRING', 'BALLOON', 'DX', 'ENDED', 'ENDORSED', 'UNIT AFTER', 'REMARKS', 'ANGIOGRAPHER', 'ANESTHESIOLOGIST', 'NURSE', 'PROCEDURE', 'TPI'])
    record_fields = records.values_list('date', 'hospital', 'first_name', 'last_name', 'middle_initial', 'age', 'sex', 'unit_before', 'category', 'is_emergency', 'swab', 'pathway', 'schedule_time_from', 'schedule_time_to', 'received', 'started', 'er_door', 'acti', 'wiring', 'balloon', 'dx', 'ended', 'endorsed', 'unit_after', 'remarks', 'angiographer', 'anesthesiologist', 'nurse', 'procedure', 'tpi')
    
    for record in record_fields:
        writer.writerow(record)

    return response

# Create function for pdf export