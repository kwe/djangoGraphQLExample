# Generated by Django 2.0.3 on 2018-03-10 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='last_name',
            field=models.CharField(default='None', max_length=200),
        ),
    ]