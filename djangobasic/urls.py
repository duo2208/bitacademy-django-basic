from django.contrib import admin
from django.urls import path

import helloword.views
import emaillist01.views
import emaillist02.views
import guestbook01.views
import guestbook02.views

urlpatterns = [
    path('', helloword.views.main, name='main'),
    path('admin/', admin.site.urls),

    path('hello1/', helloword.views.hello1, name='hello1'),
    path('tags/', helloword.views.tags, name='tags'),
    path('form/', helloword.views.form, name='form'),
    path('join', helloword.views.join, name='join'),

    path('emaillist01/', emaillist01.views.index, name='emaillist01'),
    path('emaillist01/form', emaillist01.views.form, name='emaillist01/form'),
    path('emaillist01/add', emaillist01.views.add, name='emaillist01/add'),

    path('emaillist02/', emaillist02.views.index, name='emaillist02'),
    path('emaillist02/form', emaillist02.views.form, name='emaillist02/form'),
    path('emaillist02/add', emaillist02.views.add, name='emaillist02/add'),

    path('guestbook01/', guestbook01.views.index, name='guestbook01'),
    path('guestbook01/add', guestbook01.views.add, name='guestbook01/add'),
    path('guestbook01/deleteform', guestbook01.views.deleteform, name='guestbook01/deleteform'),
    path('guestbook01/delete', guestbook01.views.delete, name='guestbook01/delete'),

    path('guestbook02/', guestbook02.views.index, name='guestbook02'),
    path('guestbook02/add', guestbook02.views.add, name='guestbook02/add'),
    path('guestbook02/deleteform', guestbook02.views.deleteform, name='guestbook02/deleteform'),
    path('guestbook02/delete', guestbook02.views.delete, name='guestbook02/delete'),
]
