# Generated by Django 3.1.7 on 2021-03-30 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_donate_closed'),
    ]

    operations = [
        migrations.AddField(
            model_name='donate',
            name='notify',
            field=models.BooleanField(default=False),
        ),
    ]
