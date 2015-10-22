# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger

from ..models.student import Student
from ..models.group import Group

def students_list(request):
	students = Student.objects.all()

	#try to order students list 
	order_by = request.GET.get('order_by', '')
	if order_by in ('id', 'last_name', 'first_name', 'ticket'):
		students = students.order_by(order_by)
		if request.GET.get('reverse', '') == '1':
			students = students.reverse()
		
	#paginate students
	paginator = Paginator(students, 3)	
	page = request.GET.get('page')
	try:
		students = paginator.page(page)
	except PageNotAnInteger:
		#If page is not integer, deliever first page
		students = paginator.page(1)
	except EmptyPage:
		#If page is out of range (e.g. 9999), deliver
		#last page of results.
		students = paginator(paginator.num_pages)

	return render(request, 'students/students_list.html', {'students': students})

def students_add(request):
	# Якщо форма була запощена:
	if request.method == "POST":

		# Якщо кнопка Додати була натиснута:
		if request.POST.get('add_button') is not None:

			# Перевіряємо дані на коректність та збираємо помилки
			errors ={}

			# перевірені дані зберігатимуться тут
			data = {'middle_name':request.POST.get('middle_name'),
							'notes': request.POST.get('notes')}

			# перевірка введених даних
			first_name = request.POST.get('first_name', '').strip()
			if not first_name:
				errors['first_name'] = u"Ім'я є обов'язковим"
			else:
				data['first_name'] = first_name

			last_name = request.POST.get('last_name', '').strip()
			if not last_name:
				errors['last_name'] = u"Прізвище є обов'язковим"
			else:
				data['last_name'] = last_name

			birthday = request.POST.get('birthday', '').strip()
			if not birthday:
				errors['birthday'] = u"Дата народження є обов'язковою"
			else:
				try: 
					datetime.strptime(birthday, '%Y-%m-%d')
				except Exception:
					errors['birthday'] = u"Введіть коректний формат дати(наприклад 1984-12-30)"
				else: data['birthday'] = birthday

			ticket = request.POST.get('ticket', '').strip()
			if not ticket:
				errors['ticket'] = u"Номер білету є обов'язковим"
			else: data['ticket'] = ticket
			
			student_group = request.POST.get('student_group', '').strip()
			if not student_group:
				errors['student_group'] = u"Оберіть групу для студента"
			else:
				groups = Group.objects.filter(pk=student_group)
				if len(groups) != 1:
					errors['student_group'] = u"Оберіть коректну групу"	
				else: data['student_group'] = student_group

			photo = request.FILES.get('photo')
			if photo:
				data['photo']= photo

			# Створюємо та зберігаємо студента в базу
			if not errors:
				student = Student(**data)
				student.save()
				# student = Student(
				# 	first_name=request.POST['first_name'],
				# 	last_name=request.POST['last_name'],
				# 	middle_name=request.POST['middle_name'],
				# 	birthday=request.POST['birthday'],
				# 	ticket=request.POST['ticket'],
				# 	student_group=Group.objects.get(pk=request.POST['student_group']),
				# 	photo=request.FILES['photo'],

				# 	)

				#зберігаємо до бази даних

				# Повертаємо користувача до списку студентів
				return HttpResponseRedirect(reverse('home'))

				# Якщо дані були введені некоректно:
			else:

				# Віддаємо шаблон форми разом із знайденими помилками
				return render(request,'students/students_add.html',
						{'groups': Group.objects.all().order_by('title'),
						'errors':errors})

			# Якщо кнопка Скасувати була натиснута:
		elif request.POST.get('cancel_button') is not None:
				# Повертаємо користувача до списку студентів
			return HttpResponseRedirect(reverse('home'))
			
		# Якщо форма не була запощена:
	else:
		return render(request, 'students/students_add.html',
			#повертаємо код початкового стану форми
			{'groups': Group.objects.all().order_by('title')})


def students_edit(request, sid):
	return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
	return HttpResponse('<h1>Delete Student %s</h1>' % sid)