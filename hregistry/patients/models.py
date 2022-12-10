from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

# Enter patient models here
class Record(models.Model):
    SWAB_STATUS = [
        ('POSITIVE','Positive'),
        ('NEGATIVE','Negative'),
        ('PENDING','Pending'),
    ]

    date = models.DateField(blank=True,null=True)
    hospital = models.BigIntegerField(blank=True,null=True,validators=[MinValueValidator(0)])
    first_name = models.CharField(blank=True,null=True,max_length=50)
    last_name = models.CharField(blank=True,null=True,max_length=50)
    middle_initial = models.CharField(blank=True,null=True,max_length=20)
    # name = models.CharField(blank=True,null=True,max_length=200)
    age = models.IntegerField(blank=True,null=True,validators=[MinValueValidator(0)])
    sex = models.CharField(blank=True,null=True,max_length=10)
    
    # unsure
    unit_before = models.CharField(blank=True,null=True,max_length=50)
    category = models.CharField(blank=True,null=True,max_length=50)

    is_emergency = models.BooleanField(blank=True,null=True,default=False)

    swab = models.CharField(blank=True,null=True,max_length=50, choices=SWAB_STATUS)
    pathway = models.BooleanField(blank=True,null=True,default=False)
    schedule_time_from = models.TimeField(blank=True,null=True)
    schedule_time_to = models.TimeField(blank=True,null=True)
    received = models.TimeField(blank=True,null=True,)
    started = models.TimeField(blank=True,null=True,)

    er_door = models.TimeField(blank=True,null=True)
    acti = models.TimeField(blank=True,null=True)
    wiring = models.TimeField(blank=True,null=True)
    balloon = models.TimeField(blank=True,null=True)

    dx = models.CharField(blank=True,null=True,max_length=50)

    # many to many
    # angiographer
    # anesthisologist
    # procedure

    ended = models.TimeField(blank=True,null=True,)
    endorsed = models.TimeField(blank=True,null=True,)
    unit_after = models.CharField(blank=True,null=True,max_length=50)
    remarks = models.CharField(blank=True,null=True,max_length=200)

    # many to many
    # nurse

    # unsure
    tpi = models.CharField(blank=True,null=True,max_length=50)


    def preop(self):
        if self.received is None or self.started is None:
            return None
        return self.received - self.started

    def cod(self):
        if self.received is None or self.acti is None:
            return None
        return self.received - self.acti

    def dtw(self):
        if self.wiring is None or self.acti is None:
            return None
        return self.wiring - self.acti
    
    def dtb(self):
        if self.balloon is None or self.acti is None:
            return None
        return self.balloon - self.acti

    def intra(self):
        if self.ended is None or self.started is None:
            return None
        return self.ended - self.started

    def post(self):
        if self.endorsed is None or self.ended is None:
            return None
        return self.endorsed - self.ended

    def cvl(self):
        if self.endorsed is None or self.received is None:
            return None
        return self.endorsed - self.received

    def __str__(self):
        if self.hospital is None:
            return 'no name'
        return self.hospital
        