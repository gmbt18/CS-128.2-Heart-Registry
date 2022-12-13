from django import forms
from django.forms import ModelChoiceField, ModelForm

from .models import *
from accounts.models import *

class StaffForm(ModelForm):
    user = ModelChoiceField(queryset=AuthUser.objects.all())

    class Meta:
        model = Staff
        fields = ['user', 'title', 'middle_initial']
    
class RecordForm(ModelForm):
    # nurse = ModelChoiceField(queryset=Staff.objects.filter(user_type=1))
    # anesthesiologist = ModelChoiceField(queryset=Staff.objects.filter(user_type=3))
    # angiographer = ModelChoiceField(queryset=Staff.objects.filter(user_type=4))
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

class EditRecordForm(ModelForm):
    # nurse = ModelChoiceField(queryset=Staff.objects.filter(user_type=1))
    # anesthesiologist = ModelChoiceField(queryset=Staff.objects.filter(user_type=3))
    # angiographer = ModelChoiceField(queryset=Staff.objects.filter(user_type=4))

    class Meta:
        model = Record
        fields = ['date', 'hospital', 'first_name', 'last_name', 'middle_initial', 'age', 'sex', 'unit_before', 'category', 
        'is_emergency', 'swab', 'pathway', 'schedule_time_from', 'schedule_time_to', 'received', 'started', 'er_door', 'acti',
        'wiring', 'balloon', 'dx', 'ended', 'endorsed', 'unit_after', 'remarks', 'angiographer', 'anesthesiologist', 'nurse',
        'procedure', 'tpi']