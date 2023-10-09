from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _

from constants import NULLABLE

User = get_user_model()


class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='habits', verbose_name=_('User'))
    place = models.CharField(max_length=255, verbose_name=_('Place'), **NULLABLE)
    time = models.TimeField(verbose_name=_('Time'), **NULLABLE)
    action = models.CharField(max_length=255, verbose_name=_('Action'))
    is_pleasant_habit = models.BooleanField(default=False, verbose_name=_('Is Pleasant Habit'), **NULLABLE)
    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL, **NULLABLE,
                                      verbose_name=_('Related Habit'))
    frequency = models.PositiveIntegerField(default=1, verbose_name=_('Frequency (days)'), **NULLABLE)
    reward = models.CharField(max_length=255, verbose_name=_('Reward'), **NULLABLE)
    estimated_time = models.PositiveIntegerField(default=2, verbose_name=_('Estimated Time (minutes)'), **NULLABLE)
    is_public = models.BooleanField(default=False, verbose_name=_('Is Public'), **NULLABLE)

    def __str__(self):
        return f'{self.user} - {self.action}'

    class Meta:
        verbose_name = _('Habit')
        verbose_name_plural = _('Habits')
