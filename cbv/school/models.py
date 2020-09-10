from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    location = models.CharField(max_length=150)
    principal = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Students(models.Model):
    name = models.CharField(max_length=40)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School,related_name='students',on_delete=models.CASCADE,)

    def __str__(self):
        return self.name