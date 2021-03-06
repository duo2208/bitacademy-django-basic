from django.db import models

# Create your models here.
class Guestbook(models.Model):
    name =  models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    message = models.CharField(max_length=4000)
    regdate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Guestbook({self.name}, {self.password}, {self.message}, {self.regdate})'
