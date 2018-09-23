# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render
from django.template import loader
from .forms import RecordForm
import os
from django.conf import settings
import requests
import json

# Create your views here.
def index(request):
	form = RecordForm()
	template = loader.get_template('predict/main.html')
	return HttpResponse(template.render({'form':form}, request))

def post(request):
	if request.method == 'POST':
		form = RecordForm(request.POST)
		if form.is_valid():
			record = [];
			for name in ["age","sex","cp","trestbps","chol","fbs","restecg","thalach","exang","oldpeak","slope","ca","thal"]:
				record.append(form.cleaned_data[name])
			url = 'https://edj1l6tdcl.execute-api.ap-southeast-1.amazonaws.com/production/heartdisease_lambda'
			payload = {
				'age':str(record[0]),
				'sex':str(record[1]),
				'cp':str(record[2]),
				'trestbps':str(record[3]),
				'chol':str(record[4]),
				'fbs':str(record[5]),
				'restecg':str(record[6]),
				'thalach':str(record[7]),
				'exang':str(record[8]),
				'oldpeak':str(record[9]),
				'slope':str(record[10]),
				'ca':str(record[11]),
				'thal':str(record[12])
			}
			result = requests.post(url,json={'record':payload})
			print(result.json())
			return JsonResponse({'result':result.json()})
	return JsonResponse({'result':-1})
