# Generated by Django 3.1.1 on 2020-09-08 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_releationship'),
    ]

    operations = [
        migrations.AlterField(
            model_name='releationship',
            name='status',
            field=models.CharField(choices=[('send', 'send'), ('accept', 'accept'), ('reject', 'reject')], max_length=6),
        ),
    ]