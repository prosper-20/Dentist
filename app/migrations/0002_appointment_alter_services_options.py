# Generated by Django 4.0.4 on 2022-05-05 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(choices=[('Teeth Whitening', 'Teeth Whitening'), ('Teeth Cleaning', 'Teeth Cleaning'), ('Braces', 'Braces'), ('Modern Anesthetic', 'Modern Anesthetic')], max_length=100)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateField()),
                ('time', models.CharField(choices=[('8:00AM', '8:00AM'), ('9:00AM', '9:00 AM'), ('10:00AM', '10:00 AM'), ('11:00AM', '11:00 AM'), ('12:00PM', '12:00 PM'), ('1:00PM', '1:00 PM'), ('2:00PM', '2:00 PM'), ('3:00PM', '3:00 PM'), ('4:00PM', '4:00 PM'), ('5:00PM', '5:00 PM'), ('6:00PM', '6:00 PM'), ('7:00PM', '7:00 PM')], max_length=100)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterModelOptions(
            name='services',
            options={'verbose_name_plural': 'Services'},
        ),
    ]
