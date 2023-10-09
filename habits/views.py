from rest_framework import viewsets
from .models import Habit
from .serializers import HabitSerializer
from .permissions import CanReadPublicHabits, IsOwnerOrReadOnly


class HabitViewSet(viewsets.ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsOwnerOrReadOnly]  # Применение кастомных прав доступа


class PublicHabitViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Habit.objects.filter(is_public=True)  # Фильтр публичных привычек
    serializer_class = HabitSerializer
    permission_classes = [CanReadPublicHabits]  # Применение кастомных прав доступа
