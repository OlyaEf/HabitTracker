# Generated by Django 4.2.6 on 2023-10-25 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0004_remove_habit_telegram_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habit',
            name='next_notification_time',
        ),
    ]