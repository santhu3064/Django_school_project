# Generated by Django 3.0.8 on 2020-09-14 19:44

from django.db import migrations, models
import school.models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.PositiveIntegerField(validators=[school.models.validate_age]),
        ),
    ]
