# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.http import HttpResponse


def students_list(request):
	students = (
		{'id':1,
		'first_name': u'Елвіс',
		'last_name': u'Преслі',
		'ticket': 235,
		'image': 'img/elvis.jpg'
		},
		{'id':1,
		'first_name': u'Фредді',
		'last_name': u'Мерк"юрі',
		'ticket': 20,
		'image': 'img/freddie.jpg'
		},
		{'id':1,
		'first_name': u'Хуліо',
		'last_name': u'Іглесіас',
		'ticket': 25,
		'image': 'img/hulio.jpg'
		},
		)
	return render(request, 'students/students_list.html', {'students': students})

def students_add(request):
	return HttpResponse('<h1>Student add form</h1>')

def students_edit(request, sid):
	return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
	return HttpResponse('<h1>Delete Student %s</h1>' % sid)

#Views for Groups		

def groups_list(request):
	return HttpResponse('<h1>Grouprs Listing</h1>')

def groups_add(request):
	return HttpResponse('<h1>Grouprs Add Form</h1>')

def groups_edit(request, gid):
	return HttpResponse('<h1>Edit Grouup %s</h1>'% gid)

def groups_delete(request, gid):
	return HttpResponse('<h1>Delete Group %s</h1>'% gid)

