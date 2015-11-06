# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.forms import ModelForm

from ..models.group import Group
from django.views.generic import UpdateView, DeleteView, CreateView
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from crispy_forms.bootstrap import FormActions
from ..models.group import Group

class GroupCreateForm(ModelForm):

    class Meta:
        model = Group
        fields = {'title', 'leader', 'notes'}

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
#Views for Groups		

def groups_list(request):
	groups = Group.objects.all()

	#try to order groups list 
	order_by = request.GET.get('order_by', '')
	if order_by in ('id', 'title', 'leader'):
		groups = groups.order_by(order_by)
		if request.GET.get('reverse', '') == '1':
			groups = groups.reverse()
	return render(request, 'students/groups_list.html', {'groups': groups})

def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)
