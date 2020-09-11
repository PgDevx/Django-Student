from django.db import models
from django.contrib.auth.models import User

class Stud(models.Model):
    name = models.OneToOneField(User, default="", on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    grade = models.CharField(max_length=20)

    def __str__(self):
        return self.name.__str__()
