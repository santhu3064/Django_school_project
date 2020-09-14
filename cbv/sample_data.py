import os
import django
from faker import Faker
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cbv.settings')

django.setup()

from school.models import School,Student

fake = Faker('en_GB')


def load_schools(n):
    for i in range(n):
        name = fake.company()
        location = fake.address()
        principal = fake.name()
        school = School.objects.get_or_create(name=name,
                                           location=location,
                                           principal=principal)[0]
        school.save()


def load_students(n):
    for i in range(n):
        name = fake.name()
        school = random.choice(School.objects.all())
        age = random.randint(10,20)
        students = Student.objects.get_or_create(name=name,
                                           age=age,
                                           school=school)

if __name__ == '__main__':
    print("Loading users")
    School.objects.all().delete()
    Student.objects.all().delete()
    load_schools(10)
    load_students(30)



