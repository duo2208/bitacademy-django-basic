from django.contrib import admin
from django.urls import path

import helloword.views
import emaillist01.views
import guestbook01.views

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

    path('guestbook01/', guestbook01.views.index, name='guestbook01'),
]
