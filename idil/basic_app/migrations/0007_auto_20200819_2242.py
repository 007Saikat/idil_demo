# Generated by Django 3.0.3 on 2020-08-19 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0006_auto_20200819_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='role',
            field=models.CharField(choices=[('A', 'admin'), ('E', 'employee')], max_length=128),
        ),
    ]
