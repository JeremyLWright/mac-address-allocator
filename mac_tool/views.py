"""
Copyright Jeremy Wright (c) 2012
Creative Commons Attribution-ShareAlike 3.0 Unported License
"""
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response, render
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate
from django.utils import simplejson

from django.forms import ModelForm, PasswordInput, CharField, ValidationError
from mac_tool.models import MacRequest, RequestUser


class ReserveMacForm(ModelForm):
    error_css_class='text-error'
    access_code_pw = CharField(label="Access Code", widget=PasswordInput(render_value=False))
    def clean_access_code_pw(self):
        print "In rcustom cleaner"
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
            return HttpResponseRedirect('/')
    else:
        form = ReserveMacForm()
    return render(request, 'reserve.html', {
        'form': form,})

