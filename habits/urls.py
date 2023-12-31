# habits/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .apps import HabitsConfig
from .views import HabitViewSet, PublicHabitViewSet

app_name = HabitsConfig.name

router = DefaultRouter()
router.register(r'habits', HabitViewSet, basename='habits')

urlpatterns = [
    path('', include(router.urls)),  # Список привычек текущего пользователя с пагинацией
    path('public-habits/', PublicHabitViewSet.as_view({'get': 'list'}), name='public_habits'),  # Список публичных привычек
    path('habits/', HabitViewSet.as_view({'post': 'create'}), name='create_habit'),  # Создание привычки
    path('habits/<int:pk>/', HabitViewSet.as_view({'patch': 'update', 'delete': 'destroy'}), name='habit_detail'),  # Редактирование и удаление привычки
] + router.urls
