from datetime import datetime
from django.db import models
from django.db.models.fields import DateField
from datetime import datetime
# Create your models here.
class Realtor(models.Model):
    
    name = models.CharField(max_length = 200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    is_MVP = models.BooleanField(default=False)
    hire_date = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name