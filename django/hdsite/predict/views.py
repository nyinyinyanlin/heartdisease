# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render
from django.template import loader
from .forms import RecordForm
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
import os
from django.conf import settings
import pickle

with open(os.path.join(settings.BASE_DIR,'trained_svm_model.pkl'), 'rb') as file:
	svc = pickle.load(file)

with open(os.path.join(settings.BASE_DIR,'scaler.pkl'), 'rb') as file:
	scaler = pickle.load(file)

# Create your views here.
def index(request):
	form = RecordForm()
	template = loader.get_template('predict/main.html')
	return HttpResponse(template.render({'form':form}, request))

def json(request):
	return JsonResponse({'name':'django','age':'1.11'})

def post(request):
	if request.method == 'POST':
		form = RecordForm(request.POST)
		if form.is_valid():
			record = [];
			for name in ["age","sex","cp","trestbps","chol","fbs","restecg","thalach","exang","oldpeak","slope","ca","thal"]:
				record.append(form.cleaned_data[name])
			print(record)
			record = scaler.transform(record)
			print(record)
			print(svc.predict([record]))
			return JsonResponse({'result':svc.predict([record])[0]})#svc.predict([record])[0]})
	return JsonResponse({'result':-1})
