# Generated by Django 4.0.4 on 2022-05-07 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_newsletter'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newsletter',
            old_name='email',
            new_name='usermail',
        ),
    ]
