from celery import shared_task
from django.utils import timezone

from .telegram_send_message import send_telegram_message


@shared_task
def send_habit_notification(habit_id, token):
    from .models import Habit
    try:
        habit = Habit.objects.get(id=habit_id)

        if habit.next_notification_time <= timezone.now():
            message = f"Пора выполнить привычку: {habit.action}"
            send_telegram_message(token, habit.telegram_id, message)

            next_notification_time = habit.next_notification_time + timezone.timedelta(days=1)
            habit.next_notification_time = next_notification_time
            habit.save()

    except Habit.DoesNotExist:
        pass
