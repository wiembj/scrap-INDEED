from django.db import models

# Create your models here.

class Table(models.Model):
    JobName = models.CharField(max_length=50)
    JobLocationCity = models.CharField(max_length=50)
    CompanyName = models.CharField(max_length=50)
    CompanyDescription = models.CharField(max_length=50)
    Estimated_salary = models.IntegerField()

