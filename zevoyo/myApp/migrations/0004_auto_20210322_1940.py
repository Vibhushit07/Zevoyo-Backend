# Generated by Django 3.1.7 on 2021-03-22 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_employee_isadmin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='custName',
            new_name='empName',
        ),
    ]
