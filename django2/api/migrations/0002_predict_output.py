# Generated by Django 3.2.3 on 2021-08-14 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='predict_output',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=50)),
                ('kabu_name', models.CharField(max_length=50)),
                ('user_name', models.CharField(max_length=50)),
            ],
        ),
    ]
