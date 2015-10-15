# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.http import HttpResponse

#Journal view
def journal(request):
		students = (
		{'id':1,
		'first_name': u'Елвіс',
		'last_name': u'Преслі',
		'ticket': 235,
		'image': 'img/elvis.jpg'},
		{'id':1,
		'first_name': u'Фредді',
		'last_name': u'Мерк"юрі',
		'ticket': 20,
		'image': 'img/freddie.jpg'},
		{'id':1,
		'first_name': u'Хуліо',
		'last_name': u'Іглесіас',
		'ticket': 25,
		'image': 'img/hulio.jpg'},
		)	
		return render(request, 'students/journal.html', {'students':students})