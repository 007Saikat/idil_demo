# Generated by Django 3.0.3 on 2020-08-20 22:45

from django.db import migrations, models
import user_admin.models


class Migration(migrations.Migration):

    dependencies = [
        ('user_admin', '0003_auto_20200821_0413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenges',
            name='applicant_status',
            field=models.CharField(default=user_admin.models.o, max_length=255),
        ),
    ]