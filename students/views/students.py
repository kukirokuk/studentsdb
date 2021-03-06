# -*- coding: utf-8 -*-
from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger

from django.forms import ModelForm
from django.views.generic import UpdateView, DeleteView, CreateView

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from crispy_forms.bootstrap import FormActions

from django import forms


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

# def students_add(request):
#     # Якщо форма була запощена:
#     if request.method == "POST":

#         # Якщо кнопка Додати була натиснута:
#         if request.POST.get('add_button') is not None:

#             # Перевіряємо дані на коректність та збираємо помилки
#             errors ={}

#             # перевірені дані зберігатимуться тут
#             data = {'middle_name':request.POST.get('middle_name'),
#                             'notes': request.POST.get('notes')}

#             # перевірка введених даних
#             first_name = request.POST.get('first_name', '').strip()
#             if not first_name:
#                 errors['first_name'] = u"Ім'я є обов'язковим"
#             else:
#                 data['first_name'] = first_name

#             last_name = request.POST.get('last_name', '').strip()
#             if not last_name:
#                 errors['last_name'] = u"Прізвище є обов'язковим"
#             else:
#                 data['last_name'] = last_name

#             birthday = request.POST.get('birthday', '').strip()
#             if not birthday:
#                 errors['birthday'] = u"Дата народження є обов'язковою"
#             else:
#                 try: 
#                     datetime.strptime(birthday, '%Y-%m-%d')
#                 except Exception:
#                     errors['birthday'] = u"Введіть коректний формат дати(наприклад 1984-12-30)"
#                 else: data['birthday'] = birthday

#             ticket = request.POST.get('ticket', '').strip()
#             if not ticket:
#                 errors['ticket'] = u"Номер білету є обов'язковим"
#             else: data['ticket'] = ticket
            
#             student_group = request.POST.get('student_group', '').strip()
#             if not student_group:
#                 errors['student_group'] = u"Оберіть групу для студента"
#             else:
#                 groups = Group.objects.filter(pk=student_group)
#                 if len(groups) != 1:
#                     errors['student_group'] = u"Оберіть коректну групу"
#                 else:
#                     data['student_group'] = groups[0]

#             photo = request.FILES.get('photo')
#             photo_name = photo.name
#             name, ext = photo_name.split('.')
#             if photo:
#                 if ext not in ['png', 'jpg']:
#                     errors['photo'] = u"Оберіть фото формату jpg  або png"

#                 else:
#                     data['photo']= photo

#             # Створюємо та зберігаємо студента в базу
#             if not errors:
#                 student = Student(**data)
#                 student.save()

#                 # Повертаємо користувача до списку студентів
#                 return HttpResponseRedirect(u'%s?status_message=Студента %s %s  успішно додано!' %(reverse('home'), data['last_name'], data['first_name']))

#                 # Якщо дані були введені некоректно:
#             else:
#                 # Віддаємо шаблон форми разом із знайденими помилками
#                 return render(request,'students/students_add.html',
#                         {'groups': Group.objects.all().order_by('title'),
#                         'errors':errors})

#             # Якщо кнопка Скасувати була натиснута:
#         elif request.POST.get('cancel_button') is not None:
#                 # Повертаємо користувача до списку студентів
#             return HttpResponseRedirect(
#                 u'%s?status_message=Додавання студента скасовано!' %reverse('home'))
            
#         # Якщо форма не була запощена:
#     else:
#         return render(request, 'students/students_add.html',
#             #повертаємо код початкового стану форми
#             {'groups': Group.objects.all().order_by('title')})


# def students_edit(request, sid):
#     return HttpResponse('<h1>Edit Student %s</h1>' % sid)

# def students_delete(request, sid):
#     return HttpResponse('<h1>Delete Student %s</h1>' % sid)


class StudentCreateForm(ModelForm):

    class Meta:
        model = Student
        fields = {'first_name', 'last_name', 'middle_name', 'student_group', 'birthday', 'photo', 'ticket', 'notes'}

    def __init__(self, *args, **kwargs):
        super(StudentCreateForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)

        # set form tag attributes
        self.helper.form_action = reverse('students_add')
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'

        # set form field properties
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'
        self.helper.render_unmentioned_fields = True
        self.helper.add_input(Submit('submit', u'Зберегти'))
        self.helper.add_input(Submit('cancel_button', u'Скасувати', css_class='btn btn-link'))

        # add buttons
        self.helper.layout[-1] = Layout(FormActions())
            

class StudentCreateView(CreateView):
    model = Student
    template_name = 'students/students_add.html'
    form_class =StudentCreateForm

    def get_success_url(self):
        return u'%s?status_message=Студента додано' % reverse('home')
 
    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(
                u'%s?status_message=Редагування скасовано!' %reverse('home'))
 
        else:
            return super(StudentCreateView, self).post(request, *args, **kwargs)


class StudentUpdateForm(ModelForm):

    class Meta:
        model = Student
        fields = {'first_name', 'last_name', 'middle_name', 'student_group', 'birthday', 'photo', 'ticket', 'notes'}

    def __init__(self, *args, **kwargs):
        super(StudentUpdateForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)

        # set form tag attributes
        self.helper.form_action = reverse('students_edit',
            kwargs={'pk': kwargs['instance'].id})
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'

        # set form field properties
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'

        self.helper.add_input(Submit('submit', u'Зберегти'))
        self.helper.add_input(Submit('cancel_button', u'Скасувати', css_class='btn btn-link'))

        # add buttons
        self.helper.layout[-1] = Layout(FormActions())

class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'students/students_edit.html'
    form_class = StudentUpdateForm
    
    def get_success_url(self):
        return u'%s?status_message=Зміни збережено' % reverse('home')
 
    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(
                u'%s?status_message=Редагування скасовано!' %reverse('home'))
 
        else:
            return super(StudentUpdateView, self).post(request, *args, **kwargs)

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/students_confirm_delete.html'

    def get_success_url(self):
        return u'%s?status_message=Студента успішно видалено!' %reverse('home')