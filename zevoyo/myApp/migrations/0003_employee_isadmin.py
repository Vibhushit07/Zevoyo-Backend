# Generated by Django 3.1.7 on 2021-03-22 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='isAdmin',
            field=models.CharField(default=1, max_length=1),
            preserve_default=False,
        ),
    ]
