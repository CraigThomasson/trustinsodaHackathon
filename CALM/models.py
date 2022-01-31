from django.db import models

# Create your models here.

class Company(models.Model):
    company_id = models.IntegerField(unique=True)
    company_name = models.CharField(max_length=200)
    company_size = models.IntegerField()
    sector = models.CharField(max_length=200)
    accreditation_level = models.CharField(max_length=100)   
