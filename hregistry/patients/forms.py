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
    nurse, anesthesiologist, angiographer = ModelMultipleChoiceField(queryset=Staff.objects.all())
    date = forms.DateField(
        widget=forms.TextInput(
            attrs={'type' : 'date'}
        )
    )

    class Meta:
        model = Record
        fields = ['date', 'hospital', 'first_name', 'last_name', 'middle_initial', 'age', 'sex', 'unit_before', 'category', 
        'is_emergency', 'swab', 'pathway', 'schedule_time_from', 'schedule_time_to', 'received', 'started', 'er_door', 'acti',
        'wiring', 'balloon', 'dx', 'ended', 'endorsed', 'unit_after', 'remarks', 'angiographer', 'anesthesiologist', 'nurse',
        'procedure', 'tpi']

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
    nurse = ModelMultipleChoiceField(queryset=Staff.objects.filter(user__user_type=1),required=False)
    anesthesiologist = ModelMultipleChoiceField(queryset=Staff.objects.filter(user__user_type=3),required=False)
    angiographer = ModelMultipleChoiceField(queryset=Staff.objects.filter(user__user_type=4),required=False)

    class Meta:
        model = Record
        fields = ['date', 'hospital', 'first_name', 'last_name', 'middle_initial', 'age', 'sex', 'unit_before', 'category', 
        'is_emergency', 'swab', 'pathway', 'schedule_time_from', 'schedule_time_to', 'received', 'started', 'er_door', 'acti',
        'wiring', 'balloon', 'dx', 'ended', 'endorsed', 'unit_after', 'remarks', 'angiographer', 'anesthesiologist', 'nurse',
        'procedure', 'tpi']

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