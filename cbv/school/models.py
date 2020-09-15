from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_age(value):
    if value >= 90:
        raise ValidationError(
            _('%(value)s age is more than enrollment age'),
            params={'value': value},
        )

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=150)
    principal = models.CharField(max_length=40)

    def get_absolute_url(self):
        return reverse('school:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=40)
    age = models.PositiveIntegerField(validators=[validate_age])
    school = models.ForeignKey(School, related_name='students', on_delete=models.CASCADE, )

    def get_absolute_url(self):
        return reverse('school:detail', kwargs={'pk': self.school.pk})


    def __str__(self):
        return self.name
