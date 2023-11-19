# Generated by Django 4.2.6 on 2023-10-09 21:17

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
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(blank=True, max_length=255, null=True, verbose_name='Place')),
                ('time', models.TimeField(blank=True, null=True, verbose_name='Время')),
                ('action', models.CharField(max_length=255, verbose_name='Действие')),
                ('is_pleasant_habit', models.BooleanField(blank=True, default=False, null=True, verbose_name='Is Pleasant Habit')),
                ('frequency', models.PositiveIntegerField(blank=True, default=1, null=True, verbose_name='Frequency (days)')),
                ('reward', models.CharField(blank=True, max_length=255, null=True, verbose_name='Reward')),
                ('estimated_time', models.PositiveIntegerField(blank=True, default=2, null=True, verbose_name='Estimated Time (minutes)')),
                ('is_public', models.BooleanField(blank=True, default=False, null=True, verbose_name='Is Public')),
                ('related_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='habits.habit', verbose_name='Related Habit')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='habits', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Habit',
                'verbose_name_plural': 'Habits',
            },
        ),
    ]
