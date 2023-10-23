from rest_framework import viewsets
from .models import Habit
from .serializers import HabitSerializer
from .permissions import CanReadPublicHabits, IsOwnerOrReadOnly


class HabitViewSet(viewsets.ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsOwnerOrReadOnly]  # Применение кастомных прав доступа

    def create(self, request, *args, **kwargs):
        #  TODO: добавить создание задачи на оповещение

        return super().create(request, *args, **kwargs)


class PublicHabitViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Habit.objects.filter(is_public=True)  # Фильтр публичных привычек
    serializer_class = HabitSerializer
    permission_classes = [CanReadPublicHabits]  # Применение кастомных прав доступа
