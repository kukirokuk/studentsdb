
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django import forms
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic.edit import FormView



from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from contact_form.forms import ContactForm

from studentsdb.settings import ADMIN_EMAIL

class CustomContactForm(ContactForm):
           
    def __init__(self, request, *args, **kwargs):
        super(CustomContactForm, self).__init__(request=request, *args, **kwargs)

        # this helper object allows us to customize form
        self.helper = FormHelper()

        # form tag attributes
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('contact_form')

        # twitter bootstrap styles
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10' 
         # form buttons
        self.helper.add_input(Submit('send_button', u'Надіслати'))

    email = forms.EmailField(
        max_length=200,
        label=u'Ваша Емейл Адреса')

    name = forms.CharField(
        label=u"Ваше ім'я",
        max_length=128)
 
    body = forms.CharField(
        label=u'Текст повідомлення',
        max_length=2560,
            widget=forms.Textarea)
    REASON = (
        ('support', u'Тех. підтримка'),
        ('feedback', u'Відгук'),
        ('delete', u'Видалення аккаунту')
    )
    reason = forms.ChoiceField(choices=REASON, label=u'Причина')
    template_name = 'contact_form/contact_form.txt'
    subject_template_name = "contact_form/contact_form_subject.txt"


class CustomContactFormView(FormView):
    form_class = CustomContactForm
    template_name = 'contact_form/contact_form.html'
 
    def form_valid(self, form):
        form.save()
        return super(CustomContactFormView, self).form_valid(form)
 
    def get_form_kwargs(self):
        # ContactForm instances require instantiation with an
        # HttpRequest.
        kwargs = super(CustomContactFormView, self).get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs
 
    def get_success_url(self):
        message = "Повідомлення успішно відправлене"
        return u'%s?status_message=%s' %(reverse('home'), message)
    def save():
        pass    
