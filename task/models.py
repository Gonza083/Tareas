
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title= models.CharField(max_length=100)
    descripcion= models.TextField(max_length=1000)
    created= models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank= True)
    importan= models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title +"- by " + self.user.username