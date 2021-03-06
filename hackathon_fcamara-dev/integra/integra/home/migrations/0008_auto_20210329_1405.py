# Generated by Django 3.1.7 on 2021-03-29 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_student_registration_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.profiletype'),
        ),
    ]
