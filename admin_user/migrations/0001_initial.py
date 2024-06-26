# Generated by Django 5.0.2 on 2024-03-28 09:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_User',
            fields=[
                ('custom_user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('user_type', models.CharField(blank=True, choices=[('Admin', 'Admin'), ('Sub-Admin', 'Sub-Admin')], max_length=50, null=True)),
                ('is_ti', models.BooleanField(default=False)),
                ('is_civil', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('account.custom_user',),
        ),
        migrations.CreateModel(
            name='Admin_OTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp', models.IntegerField(blank=True, null=True)),
                ('otp_expiry', models.DateTimeField(blank=True, null=True)),
                ('otp_type', models.CharField(blank=True, choices=[('Password', 'Password'), ('Login', 'Login')], default='Login', max_length=50, null=True)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='admin_otp', to='admin_user.admin_user')),
            ],
        ),
        migrations.CreateModel(
            name='Admin_User_Authentication_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_url', models.URLField(blank=True, null=True)),
                ('otp', models.CharField(max_length=6)),
                ('token', models.CharField(max_length=400)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_authentication', to='admin_user.admin_user')),
            ],
        ),
    ]
