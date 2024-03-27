# Generated by Django 5.0.2 on 2024-03-27 12:35

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
            name='IT_Live_Chat_Admin_Sound',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_live_chat_notification_sound', models.FileField(blank=True, null=True, upload_to='it/sound/admin_live_chat_notification_sound/')),
                ('admin_live_call_ringtone', models.FileField(blank=True, null=True, upload_to='it/sound/admin_live_call_ringtone/')),
                ('user_cannot_call_admin_sound', models.FileField(blank=True, null=True, upload_to='it/sound/user_cannot_call_admin_sound/')),
            ],
        ),
        migrations.CreateModel(
            name='IT_User_Order_Sound',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_chat_notification_tone', models.FileField(blank=True, null=True, upload_to='it/sound/order_chat_notification_tone/')),
                ('order_call_ringtone', models.FileField(blank=True, null=True, upload_to='it/sound/order_call_ringtone/')),
            ],
        ),
        migrations.CreateModel(
            name='IT_User_Sound',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website_entry_sound', models.FileField(blank=True, null=True, upload_to='it/sound/entry_sound/')),
                ('live_chat_talk_sound', models.FileField(blank=True, null=True, upload_to='it/sound/live_chat_talk_sound/')),
                ('live_chat_turned_off_sound', models.FileField(blank=True, null=True, upload_to='it/sound/live_chat_turned_off_sound/')),
                ('user_live_chat_notification_sound', models.FileField(blank=True, null=True, upload_to='it/sound/user_live_chat_notification_sound/')),
                ('user_live_call_ringtone', models.FileField(blank=True, null=True, upload_to='it/sound/user_live_call_ringtone/')),
            ],
        ),
        migrations.CreateModel(
            name='IT_CallRecording',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recording', models.FileField(upload_to='static/call_recordings/')),
                ('duration', models.DurationField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('flag', models.CharField(blank=True, max_length=255, null=True)),
                ('caller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='it_call_recordings_made', to=settings.AUTH_USER_MODEL)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='it_call_recordings_received', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='IT_ChatMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('flag', models.CharField(default='Flag', max_length=255)),
                ('admin_flag', models.CharField(default='Flag', max_length=255)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='it_received_messages', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='it_sent_messages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
