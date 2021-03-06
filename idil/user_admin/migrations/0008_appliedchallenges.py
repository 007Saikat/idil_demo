# Generated by Django 3.0.3 on 2020-08-23 08:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_admin', '0007_challenges_applicant_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppliedChallenges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(default=False)),
                ('points', models.IntegerField(default=0)),
                ('challenge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_admin.Challenges')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
