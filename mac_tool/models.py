from django.db import models
import binascii

# Create your models here.
class RequestUser(models.Model):
    added_date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    access_code = models.CharField(max_length=8)
    def __unicode__(self):
        return "{0}, {1}".format(self.last_name,self.first_name)

class FactoryLocation(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class OUI(models.Model):
    name = models.IntegerField()
    def __unicode__(self):
        return hex(self.name)
    
class MacAddress(models.Model):
    base_address = models.ForeignKey(OUI)
    production_address = models.IntegerField()
    class Meta:
        unique_together = (("base_address", "production_address"))
    def __unicode__(self):
        return hex(self.base_address.name) + hex(self.production_address)

class MacRequest(models.Model):
    req_date = models.DateTimeField(auto_now_add=True)
    requested_user = models.ForeignKey(RequestUser)
    product = models.ForeignKey(Product)
    part_number = models.CharField(max_length=200)
    programmed_at = models.ForeignKey(FactoryLocation)
    serial_number = models.CharField(max_length=200)
    die_id = models.CharField(max_length=200)
    extra_notes = models.TextField()
    mac_address = models.ForeignKey(MacAddress)
