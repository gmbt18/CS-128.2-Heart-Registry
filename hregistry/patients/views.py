from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout ,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse_lazy,reverse


from bootstrap_modal_forms.generic import BSModalDeleteView

from datetime import datetime
from .models import *
from .forms import *

from accounts.models import *
from accounts.views import indexPage, loginPage

from django.template.defaulttags import register

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

#redirects to the current year at the start of the page
@login_required(login_url='loginPage')
def indexPage(request):
    year = datetime.now().year
    return redirect(reverse_lazy('records',kwargs={'year':year}))

import csv

# Create your views here.

@login_required(login_url='loginPage')
def records(request, year):

    if request.method == "POST":
        form = RecordForm(request.POST)
        if form.is_valid:
            unsaved = form.save(commit=False)
            unsaved.calculate_fields()
            unsaved.save()

    allrecords = Record.objects.all()
    record = Record.objects.filter(date__year = year)
    record_form = RecordForm(request.GET)
    month_today = datetime.now().month
    years = (set([r.date.year for r in allrecords]))
    months = {
        1:'January',
        2:'February',
        3:'March',
        4:'April',
        5:'May',
        6:'June',
        7:'July',
        8:'August',
        9:'September',
        10:'October',
        11:'November',
        12:'December',
        }

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
# can be removed? kasi nasa modal na naman yung pag add
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
    return redirect('indexPage')

#edit record modal asynch
def editRecordPage(request, id):
    record = Record.objects.get(id=id)
    year = record.date.year
    if request.method == "POST":
        form = EditRecordForm(request.POST, instance=record)

        if form.is_valid():
            unsaved = form.save(commit=False)
            unsaved.calculate_fields()
            unsaved.save()
        return HttpResponseRedirect(reverse_lazy('records',kwargs={'year':year}))
    else:
        form = EditRecordForm(instance=record)
        context = {'form': form}
        return render(request, 'patients/edit-record.html', context)

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
    writer.writerow(['DATE', 'HOSPITAL', 'FIRST NAME', 'LAST NAME', 'MIDDLE INITIAL', 'AGE', 'SEX', 'UNIT BEFORE', 'CATEGORY', 'SWAB', 'PATHWAY', 'IS EMERGENCY', 'SCHEDULE TIME FROM', 'SCHEDULE TIME TO', 'RECEIVED', 'STARTED', 'PREOP', 'COD', 'ER DOOR', 'ACTI', 'WIRING', 'BALLOON', 'DTW', 'DTB', 'DX', 'ANGIOGRAPHER', 'ANESTHESIOLOGIST', 'PROCEDURE', 'ENDED', 'ENDORSED', 'INTRA', 'UNIT AFTER', 'REMARKS', 'NURSE', 'TPI', 'POST', 'CVL'])
    record_fields = records.values_list('date', 'hospital', 'first_name', 'last_name', 'middle_initial', 'age', 'sex', 'unit_before', 'category', 'swab', 'pathway', 'is_emergency', 'schedule_time_from', 'schedule_time_to', 'received', 'started', 'preop', 'cod', 'er_door', 'acti', 'wiring', 'balloon', 'dtw', 'dtb', 'dx', 'angiographer', 'anesthesiologist', 'procedure', 'ended', 'endorsed', 'intra', 'unit_after', 'remarks', 'nurse', 'tpi', 'post', 'cvl')
    
    for record in record_fields:
        writer.writerow(record)

    return response

# Create function for pdf export