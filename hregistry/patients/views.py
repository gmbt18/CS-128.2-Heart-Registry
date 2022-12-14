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
            form.save_m2m()

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
            print(unsaved.angiographer)
            unsaved.calculate_fields()
            unsaved.save()
            form.save_m2m()

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

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=records.csv'

    writer = csv.writer(response)
    writer.writerow(['DATE', 'HOSPITAL', 'FIRST NAME', 'LAST NAME', 'MIDDLE INITIAL', 'AGE', 'SEX', 'UNIT BEFORE', 'CATEGORY', 'SWAB', 'PATHWAY', 'IS EMERGENCY', 'SCHEDULE TIME FROM', 'SCHEDULE TIME TO', 'RECEIVED', 'STARTED', 'PREOP', 'COD', 'ER DOOR', 'ACTI', 'WIRING', 'BALLOON', 'DTW', 'DTB', 'DX', 'ANGIOGRAPHER', 'ANESTHESIOLOGIST', 'PROCEDURE', 'ENDED', 'ENDORSED', 'INTRA', 'UNIT AFTER', 'REMARKS', 'NURSE', 'TPI', 'POST', 'CVL'])
    
    for record in records:
        writer.writerow(
            [record.date, record.hospital, record.first_name, record.last_name, record.middle_initial, record.age, record.sex, record.unit_before, record.category, record.swab, record.pathway, record.is_emergency, record.schedule_time_from, record.schedule_time_to, record.received, record.started, record.preop, record.cod, record.er_door, record.acti, record.wiring, record.balloon, record.dtw, record.dtb, record.dx, '|'.join(a.user.first_name for a in record.angiographer.all()), '|'.join(a.user.first_name for a in record.anesthesiologist.all()), record.procedure, record.ended, record.endorsed, record.intra, record.unit_after, record.remarks, '|'.join(n.user.first_name for n in record.nurse.all()), record.tpi, record.post, record.cvl]
            )

    return response

# Create function for pdf export