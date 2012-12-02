"""
Copyright Jeremy Wright (c) 2013
Creative Commons Attribution-ShareAlike 3.0 Unported License
"""
from django.contrib import admin
from mac_tool.models import RequestUser, FactoryLocation, Product, OUI, MacAddress, MacRequest

class RequestUserAdmin(admin.ModelAdmin):
    pass
admin.site.register(RequestUser, RequestUserAdmin)

class FactoryLocationAdmin(admin.ModelAdmin):
    pass
admin.site.register(FactoryLocation, FactoryLocationAdmin)

class ProductAdmin(admin.ModelAdmin):
    pass
admin.site.register(Product, ProductAdmin)

class OUIAdmin(admin.ModelAdmin):
    pass
admin.site.register(OUI, OUIAdmin)

class MacAddressAdmin(admin.ModelAdmin):
    pass
admin.site.register(MacAddress, MacAddressAdmin)

class MacRequestAdmin(admin.ModelAdmin):
    pass
admin.site.register(MacRequest, MacRequestAdmin)

