# Generated by Django 3.1.7 on 2021-03-30 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20210330_1601'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='itemselection',
            unique_together={('student', 'item')},
        ),
    ]
