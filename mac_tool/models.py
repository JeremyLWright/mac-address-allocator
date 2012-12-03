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
    exhausted = models.BooleanField()
    def __unicode__(self):
        return hex(self.name)
    
class MacAddress(models.Model):
    base_address = models.ForeignKey(OUI)
    production_address = models.IntegerField()
    class Meta:
        unique_together = (("base_address", "production_address"))
    def __unicode__(self):
        oui_str = hex(self.base_address.name).lstrip("0x")
        pro_str = "{0:06X}".format(self.production_address)
        oui_parts = [oui_str[i:i+2] for i in range(0, len(oui_str), 2)]
        pro_parts = [pro_str[i:i+2] for i in range(0, len(pro_str), 2)]
        mac_parts = oui_parts + pro_parts
        formatted_mac = "{0}-{1}-{2}-{3}-{4}-{5}".format(*mac_parts)
        print formatted_mac
        return formatted_mac

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
    
    def __unicode__(self):
        return "{0}, SN:{1} Die:{2}".format(self.product, self.serial_number, self.die_id)
