# Generated by Django 3.2.3 on 2021-08-14 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_predict_output'),
    ]

    operations = [
        migrations.RenameField(
            model_name='predict_output',
            old_name='date',
            new_name='predict_date',
        ),
    ]