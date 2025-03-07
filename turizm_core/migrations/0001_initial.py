# Generated by Django 5.1.4 on 2025-01-25 12:41

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strana', models.CharField(max_length=100)),
                ('gorod', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Pasport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('familia', models.CharField(max_length=100)),
                ('imya', models.CharField(max_length=100)),
                ('otchestvo', models.CharField(max_length=100)),
                ('data_rojdenia', models.DateField()),
                ('seria', models.IntegerField()),
                ('nomer', models.IntegerField()),
                ('data_vidachi', models.DateField()),
                ('organ_vidachi', models.CharField(max_length=255)),
                ('scan_pasporta', models.ImageField(upload_to='pasports')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('opisanie', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Zagranpasport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomer', models.IntegerField()),
                ('data_vidachi', models.DateField()),
                ('organ_vidachi', models.CharField(max_length=255)),
                ('data_okonchania', models.DateField()),
                ('scan_zagranpasporta', models.ImageField(upload_to='zagranpasports')),
            ],
        ),
        migrations.CreateModel(
            name='DannieAutorizatsii',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nomer_telephona', models.CharField(max_length=15, unique=True)),
                ('rabochiy_nomer_telephona', models.CharField(default=None, max_length=15, null=True)),
                ('rabochiy_emale', models.CharField(default=None, max_length=255, null=True)),
                ('password', models.CharField(max_length=255)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='turizm_core.role')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Otel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazvanie', models.CharField(max_length=100)),
                ('opisanie', models.TextField()),
                ('kolichestvo_zvezd', models.IntegerField()),
                ('osobennosti', models.TextField()),
                ('photo', models.ImageField(upload_to='otels')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='turizm_core.address')),
            ],
        ),
        migrations.CreateModel(
            name='Turoperator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inn', models.CharField(max_length=20)),
                ('kpp', models.CharField(max_length=20)),
                ('nazvanie_companii', models.CharField(max_length=255)),
                ('dannie_autorizatsii', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Putevka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_vremya_otpravlenia', models.DateTimeField()),
                ('data_vremya_vozvrashenia', models.DateTimeField()),
                ('stoimost', models.IntegerField()),
                ('data_vremya_zaselenia', models.DateTimeField()),
                ('data_vremya_viselenia', models.DateTimeField()),
                ('otel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turizm_core.otel')),
                ('turoperator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turizm_core.turoperator')),
            ],
        ),
        migrations.CreateModel(
            name='Polzovatel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_registatsii', models.DateField(auto_now_add=True)),
                ('dannie_autorizatsii', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('pasport', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='turizm_core.pasport')),
                ('zagranpasport', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='turizm_core.zagranpasport')),
            ],
        ),
        migrations.CreateModel(
            name='Zakaz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_sozdania', models.DateField(auto_now_add=True)),
                ('status', models.IntegerField()),
                ('dop_info', models.TextField(default='')),
                ('putevka', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turizm_core.putevka')),
            ],
        ),
        migrations.CreateModel(
            name='ZakazPolzovatel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scan_dogovora', models.ImageField(upload_to='dogovors')),
                ('nomer_bileta_tuda', models.CharField(max_length=100)),
                ('nomer_bileta_obratno', models.CharField(max_length=100)),
                ('polzovatel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turizm_core.polzovatel')),
                ('zakaz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turizm_core.zakaz')),
            ],
        ),
    ]
