# Generated by Django 4.2.6 on 2023-10-14 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0002_habit_next_notification_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='telegram_id',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Telegram ID'),
        ),
    ]
