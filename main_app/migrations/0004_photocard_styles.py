# Generated by Django 3.2.7 on 2021-11-24 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20211123_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='photocard',
            name='styles',
            field=models.ManyToManyField(to='main_app.Style'),
        ),
    ]