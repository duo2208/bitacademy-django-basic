from django.contrib import admin
from django.urls import path

import helloword.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello1/', helloword.views.hello1, name='hello1'),
    path('hello2/', helloword.views.hello2, name='hello2'),
    path('tags/', helloword.views.tags, name='tags')
]
