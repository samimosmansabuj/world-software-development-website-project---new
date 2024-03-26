# Generated by Django 5.0.2 on 2024-03-19 10:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_address', models.CharField(max_length=255)),
                ('state_province', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_address', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('company_location', models.CharField(max_length=255)),
                ('company_phone_number', models.CharField(max_length=20)),
                ('company_details', models.TextField(blank=True, null=True)),
                ('company_website', models.URLField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_company_information', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SocialLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon_select', models.CharField(choices=[('Facebook', 'Facebook'), ('Linkedin', 'Linkedin'), ('Instagram', 'Instagram')], max_length=20)),
                ('url', models.URLField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_social_link', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=10, null=True)),
                ('country', models.CharField(blank=True, choices=[('Bangladesh', 'Bangladesh'), ('India', 'India'), ('US', 'US')], max_length=100, null=True)),
                ('education_qualification', models.CharField(blank=True, max_length=30, null=True)),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('occupation', models.CharField(blank=True, max_length=30, null=True)),
                ('monthly_income', models.CharField(blank=True, max_length=30, null=True)),
                ('marital_status', models.CharField(blank=True, choices=[('Maride', 'Maride'), ('Unmaride', 'Unmaride')], max_length=30, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
