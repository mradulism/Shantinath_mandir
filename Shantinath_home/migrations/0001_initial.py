# Generated by Django 3.1.4 on 2020-12-10 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Abhishek',
            fields=[
                ('Booking_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('familyname', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('contact', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=30)),
                ('pincode', models.IntegerField()),
                ('eventdate', models.DateField()),
            ],
        ),
    ]