"""
Copyright Jeremy Wright (c) 2012
Creative Commons Attribution-ShareAlike 3.0 Unported License
"""
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate
from django.utils import simplejson

def home(request):
    return render_to_response("home.html")

