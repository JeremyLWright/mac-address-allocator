from django.db import models

# Create your models here.
class RequestUser(models.Model):
    access_code = models.CharField(max_length=8)

class FactoryLocation(models.Model):
    name = models.CharField(max_length=200)

class Product(models.Model):
    name = models.CharField(max_length=200)

class MacRequestLog(models.Model):
    req_date = models.DateTimeField(auto_now_add=True)
    extra_notes = models.TextField()
    mac_address = models.BigIntegerField()
    requested_user = models.ForeignKey(RequestUser)
    part_number = models.CharField(max_length=200)
    programmed_at = models.ForeignKey(FactoryLocation)
    serial_number = models.CharField(max_length=200)
    die_id = models.CharField(max_length=200)
