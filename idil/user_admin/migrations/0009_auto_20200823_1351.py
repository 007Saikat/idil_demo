# Generated by Django 3.0.3 on 2020-08-23 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_admin', '0008_appliedchallenges'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appliedchallenges',
            name='challenge',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user_admin.Challenges'),
        ),
    ]
