from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('owner', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=15)),
                ('country', models.CharField(max_length=20)),
                ('pincode', models.IntegerField(validators=[django.core.validators.MaxLengthValidator(6), django.core.validators.MinLengthValidator(6)])),
            ],
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomType', models.CharField(choices=[('1', 'Premimum'), ('2', 'Deluxe'), ('3', 'Basic')], max_length=50)),
                ('capacity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('size', models.IntegerField()),
                ('status', models.CharField(choices=[('1', 'Available'), ('2', 'Not Available')], max_length=15)),
                ('roomNumber', models.IntegerField()),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.hotels')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkIn', models.DateField()),
                ('checkOut', models.DateField()),
                ('bookingId', models.CharField(default='null', max_length=100)),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.rooms')),
            ],
        ),
    ]
