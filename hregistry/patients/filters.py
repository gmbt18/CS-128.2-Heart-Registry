import django_filters
from django_filters import DateFilter
from django.utils import timezone
import json

from .models import Record


#Filtering the records
class RecordFilters(django_filters.FilterSet):

    date = DateFilter(field_name='date', lookup_expr='month', initial=timezone.now)
    date_year = DateFilter(field_name='date',lookup_expr='year', initial=timezone.now)

    class Meta:
        model = Record
        fields = ['date','date_year']