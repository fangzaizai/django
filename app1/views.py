# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from django.shortcuts import render
from django.http import HttpResponse
from app1.forms import MomentForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.
def moments_input(request):
	if request.method == 'POST':
		form = MomentForm(request.POST)
		if form.is_valid():
			moment = form.save()
			moment.save()
			return HttpResponseRedirect(reverse('app1.views.welcome'))
	else:
		form=MomentForm()
	PROJECT_ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	return render(request, os.path.join(PROJECT_ROOT, 'app1/templates', 'moments_input.html'), {'form': form})

def welcome(request):
	return HttpResponse("<h1>Welcome to my tiny twitter</h1>")
