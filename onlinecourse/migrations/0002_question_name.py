# Generated by Django 3.1.3 on 2022-09-10 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='name',
            field=models.CharField(default='name', max_length=200),
        ),
    ]
