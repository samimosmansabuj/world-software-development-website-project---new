# Generated by Django 5.0.2 on 2024-03-19 10:46

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
            name='CivilMetaField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Civil_Live_Chat_Admin_Sound',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_live_chat_notification_sound', models.FileField(blank=True, null=True, upload_to='civil/sound/admin_live_chat_notification_sound/')),
                ('admin_live_call_ringtone', models.FileField(blank=True, null=True, upload_to='civil/sound/admin_live_call_ringtone/')),
                ('user_cannot_call_admin_sound', models.FileField(blank=True, null=True, upload_to='civil/sound/user_cannot_call_admin_sound/')),
            ],
        ),
        migrations.CreateModel(
            name='Civil_User_Order_Sound',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_chat_notification_tone', models.FileField(blank=True, null=True, upload_to='civil/sound/order_chat_notification_tone/')),
                ('order_call_ringtone', models.FileField(blank=True, null=True, upload_to='civil/sound/order_call_ringtone/')),
            ],
        ),
        migrations.CreateModel(
            name='Civil_User_Sound',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website_entry_sound', models.FileField(blank=True, null=True, upload_to='civil/sound/entry_sound/')),
                ('live_chat_talk_sound', models.FileField(blank=True, null=True, upload_to='civil/sound/live_chat_talk_sound/')),
                ('live_chat_turned_off_sound', models.FileField(blank=True, null=True, upload_to='civil/sound/live_chat_turned_off_sound/')),
                ('user_live_chat_notification_sound', models.FileField(blank=True, null=True, upload_to='civil/sound/user_live_chat_notification_sound/')),
                ('user_live_call_ringtone', models.FileField(blank=True, null=True, upload_to='civil/sound/user_live_call_ringtone/')),
            ],
        ),
        migrations.CreateModel(
            name='Civil_Arcitecture_Images',
            fields=[
                ('civilmetafield_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='civil_dashboard.civilmetafield')),
                ('image', models.ImageField(blank=True, null=True, upload_to='civil/image/arcitecture-image/')),
            ],
            bases=('civil_dashboard.civilmetafield',),
        ),
        migrations.CreateModel(
            name='Civil_BlogCard',
            fields=[
                ('civilmetafield_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='civil_dashboard.civilmetafield')),
                ('image', models.ImageField(blank=True, null=True, upload_to='civil/image/blog-card/')),
                ('title', models.CharField(max_length=100)),
                ('tag', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('is_active', models.BooleanField(default=False)),
            ],
            bases=('civil_dashboard.civilmetafield',),
        ),
        migrations.CreateModel(
            name='Civil_CardTemplate',
            fields=[
                ('civilmetafield_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='civil_dashboard.civilmetafield')),
                ('image', models.ImageField(blank=True, null=True, upload_to='civil/image/template-card/')),
                ('title', models.CharField(max_length=100)),
                ('tag', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=5, max_digits=10)),
                ('url', models.URLField()),
                ('is_active', models.BooleanField(default=False)),
            ],
            bases=('civil_dashboard.civilmetafield',),
        ),
        migrations.CreateModel(
            name='Civil_Company_Member',
            fields=[
                ('civilmetafield_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='civil_dashboard.civilmetafield')),
                ('image', models.ImageField(blank=True, null=True, upload_to='civil/image/company-member/')),
                ('name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=150)),
                ('phone_number', models.CharField(max_length=14)),
                ('address', models.CharField(max_length=500)),
            ],
            bases=('civil_dashboard.civilmetafield',),
        ),
        migrations.CreateModel(
            name='Civil_Contact_Us',
            fields=[
                ('civilmetafield_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='civil_dashboard.civilmetafield')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=150)),
                ('phone_number', models.CharField(max_length=15)),
                ('subject', models.CharField(max_length=600)),
                ('message', models.TextField()),
            ],
            bases=('civil_dashboard.civilmetafield',),
        ),
        migrations.CreateModel(
            name='Civil_Feature_Work_Category',
            fields=[
                ('civilmetafield_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='civil_dashboard.civilmetafield')),
                ('title', models.CharField(max_length=150)),
            ],
            bases=('civil_dashboard.civilmetafield',),
        ),
        migrations.CreateModel(
            name='Civil_Footer_Section_Topics',
            fields=[
                ('civilmetafield_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='civil_dashboard.civilmetafield')),
                ('title', models.CharField(max_length=50)),
                ('topic_url', models.URLField()),
                ('description', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=False)),
            ],
            bases=('civil_dashboard.civilmetafield',),
        ),
        migrations.CreateModel(
            name='Civil_FourCardSection',
            fields=[
                ('civilmetafield_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='civil_dashboard.civilmetafield')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='civil/image/four-card-icons/')),
                ('title', models.CharField(max_length=100)),
                ('tag', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            bases=('civil_dashboard.civilmetafield',),
        ),
        migrations.CreateModel(
            name='Civil_Global_Location',
            fields=[
                ('civilmetafield_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='civil_dashboard.civilmetafield')),
                ('flag_logo', models.ImageField(blank=True, null=True, upload_to='civil/image/global-location-flag/')),
                ('country_name', models.CharField(max_length=30)),
                ('office_address', models.CharField(max_length=400)),
                ('contact_details', models.CharField(max_length=400)),
                ('is_active', models.BooleanField(default=False)),
            ],
            bases=('civil_dashboard.civilmetafield',),
        ),
        migrations.CreateModel(
            name='Civil_Homepage_Segment',
            fields=[
                ('civilmetafield_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='civil_dashboard.civilmetafield')),
                ('photo_or_video', models.FileField(blank=True, null=True, upload_to='civil/image/segment/')),
            ],
            bases=('civil_dashboard.civilmetafield',),
        ),
        migrations.CreateModel(
            name='Civil_Notice_Board',
            fields=[
                ('civilmetafield_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='civil_dashboard.civilmetafield')),
                ('title', models.CharField(max_length=500)),
                ('date', models.DateField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Active', 'Active'), ('Deactivate', 'Deactivate'), ('Expired', 'Expired')], default='Active', max_length=50)),
                ('file', models.FileField(blank=True, null=True, upload_to='civil/file/notice-board/')),
                ('is_active', models.BooleanField(default=False)),
            ],
            bases=('civil_dashboard.civilmetafield',),
        ),
        migrations.CreateModel(
            name='Civil_Office_Address',
            fields=[
                ('civilmetafield_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='civil_dashboard.civilmetafield')),
                ('address', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=140)),
                ('phone', models.CharField(max_length=14)),
                ('fax', models.CharField(max_length=20)),
            ],
            bases=('civil_dashboard.civilmetafield',),
        ),
        migrations.CreateModel(
            name='Civil_Order_Card',
            fields=[
                ('civilmetafield_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='civil_dashboard.civilmetafield')),
                ('title', models.CharField(max_length=500)),
                ('image', models.ImageField(blank=True, null=True, upload_to='civil/image/order-card/')),
                ('file', models.FileField(blank=True, null=True, upload_to='civil/file/order-card/')),
                ('is_active', models.BooleanField(default=False)),
            ],
            bases=('civil_dashboard.civilmetafield',),
        ),
        migrations.CreateModel(
            name='Civil_Our_Services',
            fields=[
                ('civilmetafield_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='civil_dashboard.civilmetafield')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='civil/image/services-icons/')),
                ('title', models.CharField(max_length=500)),
                ('tags', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=False)),
            ],
            bases=('civil_dashboard.civilmetafield',),
        ),
        migrations.CreateModel(
            name='Civil_Payment_Logo',
            fields=[
                ('civilmetafield_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='civil_dashboard.civilmetafield')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='civil/image/payment-logo/')),
            ],
            bases=('civil_dashboard.civilmetafield',),
        ),
        migrations.CreateModel(
            name='Civil_Security_Page',
            fields=[
                ('civilmetafield_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='civil_dashboard.civilmetafield')),
                ('description', models.TextField(blank=True, null=True)),
            ],
            bases=('civil_dashboard.civilmetafield',),
        ),
        migrations.CreateModel(
            name='Civil_Social_Media',
            fields=[
                ('civilmetafield_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='civil_dashboard.civilmetafield')),
                ('name', models.CharField(max_length=150)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='civil/image/social-media-icon/')),
                ('url', models.URLField(max_length=500)),
            ],
            bases=('civil_dashboard.civilmetafield',),
        ),
        migrations.CreateModel(
            name='Civil_Subscriptions',
            fields=[
                ('civilmetafield_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='civil_dashboard.civilmetafield')),
                ('email', models.EmailField(max_length=150)),
            ],
            bases=('civil_dashboard.civilmetafield',),
        ),
        migrations.CreateModel(
            name='Civil_Support_Company_Logo',
            fields=[
                ('civilmetafield_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='civil_dashboard.civilmetafield')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='civil/image/comapny-logo/')),
            ],
            bases=('civil_dashboard.civilmetafield',),
        ),
        migrations.CreateModel(
            name='Civil_ThreeCardSection',
            fields=[
                ('civilmetafield_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='civil_dashboard.civilmetafield')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='civil/image/three-card-icons/')),
                ('title', models.CharField(max_length=100)),
                ('tag', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            bases=('civil_dashboard.civilmetafield',),
        ),
        migrations.CreateModel(
            name='Civil_TimeData',
            fields=[
                ('civilmetafield_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='civil_dashboard.civilmetafield')),
                ('year', models.PositiveSmallIntegerField()),
                ('month', models.PositiveSmallIntegerField()),
                ('day', models.PositiveSmallIntegerField()),
                ('hour', models.PositiveSmallIntegerField()),
                ('second', models.PositiveSmallIntegerField()),
            ],
            bases=('civil_dashboard.civilmetafield',),
        ),
        migrations.CreateModel(
            name='Civil_TwoCardCustomerFeedback',
            fields=[
                ('civilmetafield_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='civil_dashboard.civilmetafield')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='civil/image/two-card-customer-feedback/')),
                ('title', models.CharField(max_length=100)),
                ('tag', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
            bases=('civil_dashboard.civilmetafield',),
        ),
        migrations.CreateModel(
            name='Civil_WebsiteBanner',
            fields=[
                ('civilmetafield_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='civil_dashboard.civilmetafield')),
                ('header', models.CharField(max_length=100)),
                ('tag', models.CharField(max_length=100)),
                ('image_and_video', models.FileField(blank=True, null=True, upload_to='civil/image/banners/')),
            ],
            bases=('civil_dashboard.civilmetafield',),
        ),
        migrations.CreateModel(
            name='Civil_WebsiteLogo',
            fields=[
                ('civilmetafield_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='civil_dashboard.civilmetafield')),
                ('image', models.ImageField(blank=True, null=True, upload_to='civil/image/logo/')),
            ],
            bases=('civil_dashboard.civilmetafield',),
        ),
        migrations.CreateModel(
            name='Civil_CallRecording',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recording', models.FileField(upload_to='static/call_recordings/')),
                ('duration', models.DurationField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('flag', models.CharField(blank=True, max_length=255, null=True)),
                ('caller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='civil_call_recordings_made', to=settings.AUTH_USER_MODEL)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='civil_call_recordings_received', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Civil_ChatMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('flag', models.CharField(default='Flag', max_length=255)),
                ('admin_flag', models.CharField(default='Flag', max_length=255)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='civil_received_messages', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='civil_sent_messages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Civil_Arcitecture',
            fields=[
                ('civilmetafield_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='civil_dashboard.civilmetafield')),
                ('title', models.CharField(max_length=150)),
                ('plan_details', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('describtion', models.TextField()),
                ('feature_image', models.ManyToManyField(to='civil_dashboard.civil_arcitecture_images')),
            ],
            bases=('civil_dashboard.civilmetafield',),
        ),
        migrations.CreateModel(
            name='Civil_Feature_Work',
            fields=[
                ('civilmetafield_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='civil_dashboard.civilmetafield')),
                ('image', models.ImageField(blank=True, null=True, upload_to='civil/image/feature-work-image/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feature_work_category', to='civil_dashboard.civil_feature_work_category')),
            ],
            bases=('civil_dashboard.civilmetafield',),
        ),
        migrations.CreateModel(
            name='Civil_Footer_Section_3',
            fields=[
                ('civilmetafield_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='civil_dashboard.civilmetafield')),
                ('title', models.CharField(max_length=50)),
                ('topics', models.ManyToManyField(to='civil_dashboard.civil_footer_section_topics')),
            ],
            bases=('civil_dashboard.civilmetafield',),
        ),
        migrations.CreateModel(
            name='Civil_Footer_Section_2',
            fields=[
                ('civilmetafield_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='civil_dashboard.civilmetafield')),
                ('title', models.CharField(max_length=50)),
                ('topics', models.ManyToManyField(to='civil_dashboard.civil_footer_section_topics')),
            ],
            bases=('civil_dashboard.civilmetafield',),
        ),
        migrations.CreateModel(
            name='Civil_Footer_Section_1',
            fields=[
                ('civilmetafield_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='civil_dashboard.civilmetafield')),
                ('title', models.CharField(max_length=50)),
                ('topics', models.ManyToManyField(to='civil_dashboard.civil_footer_section_topics')),
            ],
            bases=('civil_dashboard.civilmetafield',),
        ),
    ]