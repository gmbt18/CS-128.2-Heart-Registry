from django import forms
from django.forms import ModelChoiceField, ModelForm,ModelMultipleChoiceField

from .models import *
from accounts.models import *

class StaffForm(ModelForm):
    user = ModelChoiceField(queryset=AuthUser.objects.all())

    class Meta:
        model = Staff
        fields = ['user', 'title', 'middle_initial']
    
class RecordForm(ModelForm):
    nurse = ModelMultipleChoiceField(queryset=Staff.objects.all(), required=False)
    anesthesiologist = ModelMultipleChoiceField(queryset=Staff.objects.all(), required=False)
    angiographer = ModelMultipleChoiceField(queryset=Staff.objects.all(), required=False)

    # date = forms.DateField(
    #     widget=forms.TextInput(
    #         attrs={'type' : 'date'}
    #     )
    # )

    class Meta:
        model = Record
        fields = ['date', 'hospital', 'first_name', 'last_name', 'middle_initial', 'age', 'sex', 'unit_before', 'category', 
        'is_emergency', 'swab', 'pathway', 'schedule_time_from', 'schedule_time_to', 'received', 'started', 'er_door', 'acti',
        'wiring', 'balloon', 'dx', 'ended', 'endorsed', 'unit_after', 'remarks', 'angiographer', 'anesthesiologist', 'nurse',
        'procedure', 'tpi']

        widgets = {
            'date' : forms.TextInput(attrs={'type':'date'}),
            # 'is_emergency' : forms.CheckboxInput(),
            # 'pathway' : forms.CheckboxInput(),
            'schedule_time_from' : forms.TextInput(attrs={'type':'time'}),
            'schedule_time_to' : forms.TextInput(attrs={'type':'time'}),
            'received' : forms.TextInput(attrs={'type':'time'}),
            'started' : forms.TextInput(attrs={'type':'time'}),
            'er_door' : forms.TextInput(attrs={'type':'time'}),
            'acti' : forms.TextInput(attrs={'type':'time'}),
            'wiring' : forms.TextInput(attrs={'type':'time'}),
            'balloon' : forms.TextInput(attrs={'type':'time'}),
            'ended' : forms.TextInput(attrs={'type':'time'}),
            'endorsed' : forms.TextInput(attrs={'type':'time'}),
        }

        labels = {
            'date':'Date',
            'hospital':'Hospital',
            'first_name':'First Name',
            'last_name':'Last Name',
            'middle_initial':'M.I.',
            'age':'Age',
            'sex':'Sex',
            'unit_before':'Unit Before',
            'category':'Category',
            'is_emergency':'Is Emergency',
            'swab':'Swab Test',
            'pathway':'Pathway',
            'schedule_time_from':'Scheduled Time From',
            'schedule_time_to':'Scheduled Time To',
            'received':'Time Received',
            'started':'Time Started',
            'er_door':'ER Door',
            'acti':'ACTI',
            'wiring':'Wiring',
            'balloon':'Balloon',
            'dx':'DX',
            'ended':'Ended',
            'endorsed':'Endorsed',
            'unit_after':'Unit After',
            'remarks':'Remarks',
            'angiographer':'Angiographer',
            'anesthesiologist':'Anesthesiologist',
            'nurse':'Nurse',
            'procedure':'Procedure',
            'tpi':'TPI',
        }

class EditRecordForm(ModelForm):
    nurse = ModelMultipleChoiceField(queryset=Staff.objects.all(), required=False)
    anesthesiologist = ModelMultipleChoiceField(queryset=Staff.objects.all(), required=False)
    angiographer = ModelMultipleChoiceField(queryset=Staff.objects.all(), required=False)

    class Meta:
        model = Record
        fields = ['date', 'hospital', 'first_name', 'last_name', 'middle_initial', 'age', 'sex', 'unit_before', 'category', 
        'is_emergency', 'swab', 'pathway', 'schedule_time_from', 'schedule_time_to', 'received', 'started', 'er_door', 'acti',
        'wiring', 'balloon', 'dx', 'ended', 'endorsed', 'unit_after', 'remarks', 'angiographer', 'anesthesiologist', 'nurse',
        'procedure', 'tpi']

        widgets = {
            'date' : forms.TextInput(attrs={'type':'date'}),
            # 'is_emergency' : forms.CheckboxInput(),
            # 'pathway' : forms.CheckboxInput(),
            'schedule_time_from' : forms.TextInput(attrs={'type':'time'}),
            'schedule_time_to' : forms.TextInput(attrs={'type':'time'}),
            'received' : forms.TextInput(attrs={'type':'time'}),
            'started' : forms.TextInput(attrs={'type':'time'}),
            'er_door' : forms.TextInput(attrs={'type':'time'}),
            'acti' : forms.TextInput(attrs={'type':'time'}),
            'wiring' : forms.TextInput(attrs={'type':'time'}),
            'balloon' : forms.TextInput(attrs={'type':'time'}),
            'ended' : forms.TextInput(attrs={'type':'time'}),
            'endorsed' : forms.TextInput(attrs={'type':'time'}),
        }

        labels = {
            'date':'Date',
            'hospital':'Hospital',
            'first_name':'First Name',
            'last_name':'Last Name',
            'middle_initial':'M.I.',
            'age':'Age',
            'sex':'Sex',
            'unit_before':'Unit Before',
            'category':'Category',
            'is_emergency':'Is Emergency',
            'swab':'Swab Test',
            'pathway':'Pathway',
            'schedule_time_from':'Scheduled Time From',
            'schedule_time_to':'Scheduled Time To',
            'received':'Time Received',
            'started':'Time Started',
            'er_door':'ER Door',
            'acti':'ACTI',
            'wiring':'Wiring',
            'balloon':'Balloon',
            'dx':'DX',
            'ended':'Ended',
            'endorsed':'Endorsed',
            'unit_after':'Unit After',
            'remarks':'Remarks',
            'angiographer':'Angiographer',
            'anesthesiologist':'Anesthesiologist',
            'nurse':'Nurse',
            'procedure':'Procedure',
            'tpi':'TPI',
        }
