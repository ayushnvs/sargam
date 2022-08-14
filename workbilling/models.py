from django.db import models
import datetime

# Create your models here.
class Billing(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    hours = models.CharField(max_length=5, default='00:00')
    date = models.DateField(default=datetime.date.today)
    billingdate = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)

    def __str__(self):
        return self.title