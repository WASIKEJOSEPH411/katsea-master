# Generated by Django 3.2.5 on 2021-07-18 21:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, null=True, unique=True, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, unique=True)),
                ('title', models.CharField(choices=[('pr', 'President'), ('vp', 'Vice President'), ('sg', 'Secretary General'), ('vs', 'Vice Secretary'), ('tr', 'Treasurer'), ('dt', 'Deputy Treasurer'), ('os', 'Organizing Secretary'), ('eas', 'External Affairs Secretary'), ('ers', 'Education and Research Secretary'), ('ad', 'Auditor'), ('tru', 'Trustees')], max_length=5)),
                ('count', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('code', models.CharField(max_length=6, null=True, unique=True)),
                ('status', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Ballot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pr', models.CharField(max_length=254)),
                ('vp', models.CharField(max_length=254)),
                ('sg', models.CharField(max_length=254)),
                ('vs', models.CharField(max_length=254)),
                ('tr', models.CharField(max_length=254)),
                ('dt', models.CharField(max_length=254)),
                ('os', models.CharField(max_length=254)),
                ('eas', models.CharField(max_length=254)),
                ('ers', models.CharField(max_length=254)),
                ('ad', models.CharField(max_length=254)),
                ('tru1', models.CharField(max_length=254)),
                ('tru2', models.CharField(max_length=254)),
                ('tru3', models.CharField(max_length=254)),
                ('voter', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainapp.voter')),
            ],
        ),
    ]
