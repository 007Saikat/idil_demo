# Generated by Django 3.0.3 on 2020-08-19 18:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import user_admin.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(default='admin', max_length=128)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to=user_admin.models.path_and_rename)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
