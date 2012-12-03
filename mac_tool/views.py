"""
Copyright Jeremy Wright (c) 2012
Creative Commons Attribution-ShareAlike 3.0 Unported License
"""
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response, render
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate
from django.utils import simplejson

from django.forms import ModelForm, PasswordInput, CharField, ValidationError
from mac_tool.models import MacRequest, RequestUser, OUI, MacAddress
from django.db.models import Max

class ReserveMacForm(ModelForm):
    error_css_class='text-error'
    access_code_pw = CharField(label="Access Code", widget=PasswordInput(render_value=False))
    def clean_access_code_pw(self):
        data = self.cleaned_data['access_code_pw']
        try:
            if(RequestUser.objects.filter(access_code=data).count() < 1):
                raise ValidationError("Please use a valid Access Code")
        except(ObjectDoesNotExist):
            raise ValidationError("Please use a valid Access Code")
        return data

    class Meta:
        model = MacRequest
        exclude = ('mac_address', 'requested_user')


def reserve(request):
    if request.method == 'POST':
        form = ReserveMacForm(request.POST)
        if form.is_valid():
            #We don't want to use the form's save. We need to do some sepcial processing
            request = MacRequest()
            request.requested_user = RequestUser.objects.get(access_code=form.cleaned_data['access_code_pw'])
            request.product = form.cleaned_data['product']
            request.part_number = form.cleaned_data['part_number']
            request.programmed_at = form.cleaned_data['programmed_at']
            request.serial_number = form.cleaned_data['serial_number']
            request.die_id = form.cleaned_data['die_id']
            request.extra_notes = form.cleaned_data['extra_notes']

            oui = OUI.objects.filter(exhausted=False)[0]

            mac = MacAddress()
            current_max = MacAddress.objects.filter(base_address=oui).all().aggregate(Max('production_address'))
            mac.base_address = oui
            if(current_max['production_address__max'] == None):
                mac.production_address = 0
            else:
                mac.production_address = current_max['production_address__max'] + 1
            mac.save()
            request.mac_address = mac
            request.save()

            return HttpResponseRedirect('/mac/show/?mac_id='+str(mac.id))
    else:
        form = ReserveMacForm()
    return render(request, 'reserve.html', {
        'form': form,})
    
def show(request):
    mac_id = request.GET['mac_id']
    address = MacAddress.objects.filter(id=mac_id).get()
    print address
    return HttpResponse(address)

