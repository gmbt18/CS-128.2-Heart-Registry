from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

# Enter patient models here
class Angiographer(models.Model):
    title = models.CharField(default="Dr.",blank=True,max_length=10)
    first_name = models.CharField(blank=True,max_length=50)
    last_name = models.CharField(blank=True,max_length=50)
    middle_initial = models.CharField(blank=True,max_length=20)

    def __str__(self):
        return "{} {} {} {}".format(self.title,self.first_name,self.last_name,self.middle_initial)

    def get_short_name(self):
        return "{} {}. {}".format(self.title, self.first_name[0], self.last_name)


class Anesthesiologist(models.Model):
    title = models.CharField(default="Dr.",blank=True,max_length=10)
    first_name = models.CharField(blank=True,max_length=50)
    last_name = models.CharField(blank=True,max_length=50)
    middle_initial = models.CharField(blank=True,max_length=20)

    def __str__(self):
        return "{} {} {} {}".format(self.title,self.first_name,self.last_name,self.middle_initial)

    def get_short_name(self):
        return "{} {}. {}".format(self.title, self.first_name[0], self.last_name)

class Nurse(models.Model):
    first_name = models.CharField(blank=True,max_length=50)
    last_name = models.CharField(blank=True,max_length=50)
    middle_initial = models.CharField(blank=True,max_length=20)

    def __str__(self):
        return "{} {} {}".format(self.first_name,self.last_name,self.middle_initial)

class Category(models.Model):
    name = models.CharField(blank=True,max_length=50)
    
    def __str__(self):
        return self.name

class Procedure(models.Model):
    name = models.CharField(blank=True,max_length=50)
    
    def __str__(self):
        return self.name


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
    unit_before = models.CharField(blank=True,null=True,max_length=50)
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
    ended = models.TimeField(blank=True,null=True,)
    endorsed = models.TimeField(blank=True,null=True,)
    unit_after = models.CharField(blank=True,null=True,max_length=50)
    remarks = models.CharField(blank=True,null=True,max_length=200)

    category = models.CharField(blank=True,null=True,max_length=50)
    procedure = models.CharField(blank=True,null=True,max_length=50)

    # many-to-many fields
    angiographer = models.ManyToManyField(Angiographer)
    anesthesiologist = models.ManyToManyField(Anesthesiologist)
    nurse = models.ManyToManyField(Nurse)
    # category = models.ManyToManyField(Category)
    # procedure = models.ManyToManyField(Procedure)

    # unsure
    tpi = models.CharField(blank=True,null=True,max_length=50)


    def get_preop(self):
        if self.received is None or self.started is None:
            return None
        return self.received - self.started

    def get_cod(self):
        if self.received is None or self.acti is None:
            return None
        return self.received - self.acti

    def get_dtw(self):
        if self.wiring is None or self.acti is None:
            return None
        return self.wiring - self.acti
    
    def get_dtb(self):
        if self.balloon is None or self.acti is None:
            return None
        return self.balloon - self.acti

    def get_intra(self):
        if self.ended is None or self.started is None:
            return None
        return self.ended - self.started

    def get_post(self):
        if self.endorsed is None or self.ended is None:
            return None
        return self.endorsed - self.ended

    def get_cvl(self):
        if self.endorsed is None or self.received is None:
            return None
        return self.endorsed - self.received

    def __str__(self):
        if self.hospital is None:
            return 'no name'
        return self.hospital
        