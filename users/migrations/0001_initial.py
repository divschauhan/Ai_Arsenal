# Generated by Django 3.1.6 on 2021-05-04 08:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DOB', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE')], max_length=10)),
                ('phone', models.IntegerField()),
                ('add', models.CharField(default='user address', max_length=80)),
                ('city', models.TextField(default='not available', max_length=20)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
