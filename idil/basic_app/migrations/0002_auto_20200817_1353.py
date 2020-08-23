# Generated by Django 3.0.3 on 2020-08-17 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetail',
            name='picture',
        ),
        migrations.AddField(
            model_name='userdetail',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics'),
        ),
        migrations.AddField(
            model_name='userdetail',
            name='role',
            field=models.CharField(default='employee', max_length=100),
        ),
    ]