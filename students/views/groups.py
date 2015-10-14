# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.http import HttpResponse

#Views for Groups		

# def groups_list(request):
# 	groups = (
# 		{'id': 1,
# 		'name': u'MMM-11',
# 		'leader': u'Елвіс Преслі'
# 		},
# 		{'id': 2,
# 		'name': u'MMM-21',
# 		'leader': u'Фредді Мерк"юрі'
# 		},
# 		{'id': 3,
# 		'name': u'MMM-31',
# 		'leader': u'Хуліо Іглесіас'
# 		},
# 		)
# 	return render(request, 'students/groups_list.html' {'groups': groups})

def groups_list(request):
    groups = (
        {'id': 1,
         'name': u'МММ-11',
         'leader': u'Елвіс Преслі'
         },
        {'id': 2,
         'name': u'МММ-21',
         'leader': u'Фредді Мерк"юрі'
         },
         {'id': 3,
         'name': u'МММ-31',
         'leader': u'Хуліо Іглесіас'
         },
         )
    return render(request, 'students/groups_list.html', {'groups': groups})

def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)