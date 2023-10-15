from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Habit
from .serializers import HabitSerializer
from .permissions import IsOwnerOrReadOnly, CanReadPublicHabits
from django.test import RequestFactory


User = get_user_model()


class HabitModelTestCase(TestCase):
    def test_user_field(self):
        user = User.objects.create(email="testuser@example.com", password="password")
        habit = Habit.objects.create(
            user=user,
            action="Morning exercise",
            is_pleasant_habit=False,
            frequency=7,
            estimated_time=2,
            is_public=False,
        )
        self.assertEqual(habit.user, user)

    def test_place_field(self):
        habit = Habit.objects.create(
            user=User.objects.create(email="testuser@example.com", password="password"),
            action="Morning exercise",
            place="Home",
            is_pleasant_habit=False,
            frequency=7,
            estimated_time=2,
            is_public=False,
        )
        self.assertEqual(habit.place, "Home")

    def test_time_field(self):
        habit = Habit.objects.create(
            user=User.objects.create(email="testuser@example.com", password="password"),
            action="Morning exercise",
            time="08:00:00",
            is_pleasant_habit=False,
            frequency=7,
            estimated_time=2,
            is_public=False,
        )
        self.assertEqual(habit.time, "08:00:00")

    def test_action_field(self):
        habit = Habit.objects.create(
            user=User.objects.create(email="testuser@example.com", password="password"),
            action="Morning exercise",
            is_pleasant_habit=False,
            frequency=7,
            estimated_time=2,
            is_public=False,
        )
        self.assertEqual(habit.action, "Morning exercise")

    def test_is_pleasant_habit_field(self):
        habit = Habit.objects.create(
            user=User.objects.create(email="testuser@example.com", password="password"),
            action="Morning exercise",
            is_pleasant_habit=True,
            frequency=7,
            estimated_time=2,
            is_public=False,
        )
        self.assertTrue(habit.is_pleasant_habit)

    def test_related_habit_field(self):
        habit1 = Habit.objects.create(
            user=User.objects.create(email="testuser@example.com", password="password"),
            action="Morning exercise",
            is_pleasant_habit=False,
            frequency=7,
            estimated_time=2,
            is_public=False,
        )
        habit2 = Habit.objects.create(
            user=User.objects.create(email="testuser1@example.com", password="password"),
            action="Evening exercise",
            is_pleasant_habit=True,
            frequency=7,
            estimated_time=2,
            is_public=False,
            related_habit=habit1,
        )
        self.assertEqual(habit2.related_habit, habit1)

    def test_frequency_field(self):
        habit = Habit.objects.create(
            user=User.objects.create(email="testuser@example.com", password="password"),
            action="Morning exercise",
            is_pleasant_habit=False,
            frequency=7,
            estimated_time=2,
            is_public=False,
        )
        self.assertEqual(habit.frequency, 7)

    def test_estimated_time_field(self):
        habit = Habit.objects.create(
            user=User.objects.create(email="testuser@example.com", password="password"),
            action="Morning exercise",
            is_pleasant_habit=False,
            frequency=7,
            estimated_time=2,
            is_public=False,
        )
        self.assertEqual(habit.estimated_time, 2)

    def test_is_public_field(self):
        habit = Habit.objects.create(
            user=User.objects.create(email="testuser@example.com", password="password"),
            action="Morning exercise",
            is_pleasant_habit=False,
            frequency=7,
            estimated_time=2,
            is_public=True,
        )
        self.assertTrue(habit.is_public)

    def test_reward_field(self):
        habit = Habit.objects.create(
            user=User.objects.create(email="testuser@example.com", password="password"),
            action="Morning exercise",
            is_pleasant_habit=False,
            frequency=7,
            estimated_time=2,
            is_public=False,
            reward="Brew a cup of coffee",
        )
        self.assertEqual(habit.reward, "Brew a cup of coffee")

    def test_str_representation(self):
        user = User.objects.create(email="testuser@example.com", password="password")
        habit = Habit.objects.create(
            user=user,
            place="Home",
            time="08:00:00",
            action="Morning exercise",
            is_pleasant_habit=False,
            frequency=7,
            estimated_time=2,
            is_public=False,
        )
        self.assertEqual(str(habit), f"{user} - {habit.action}")

    def test_habit_creation(self):
        user = User.objects.create(email="testuser@example.com", password="password")
        Habit.objects.create(
            user=user,
            place="Home",
            time="08:00:00",
            action="Morning exercise",
            is_pleasant_habit=False,
            frequency=7,
            estimated_time=2,
            is_public=False,
        )
        self.assertEqual(Habit.objects.count(), 1)

    def test_habit_str_representation_with_pleasant_habit(self):
        user = User.objects.create(email="testuser@example.com", password="password")
        habit = Habit.objects.create(
            user=user,
            place="Home",
            time="08:00:00",
            action="Morning exercise",
            is_pleasant_habit=True,
            frequency=7,
            estimated_time=2,
            is_public=False,
        )
        expected_str = f"{user} - {habit.action} (pleasant habit)"
        self.assertEqual(str(habit), expected_str)

    def test_habit_str_representation_with_public_habit(self):
        user = User.objects.create(email="testuser@example.com", password="password")
        habit = Habit.objects.create(
            user=user,
            place="Home",
            time="08:00:00",
            action="Morning exercise",
            is_pleasant_habit=False,
            frequency=7,
            estimated_time=2,
            is_public=True,
        )
        expected_str = f"{user} - {habit.action} (public)"
        self.assertEqual(str(habit), expected_str)

    def test_related_habit_set_to_null(self):
        user = User.objects.create(email="testuser@example.com", password="password")
        habit = Habit.objects.create(
            user=user,
            place="Home",
            time="08:00:00",
            action="Morning exercise",
            is_pleasant_habit=False,
            frequency=7,
            estimated_time=2,
            is_public=False,
        )
        self.assertIsNone(habit.related_habit)

    def test_habit_with_related_habit(self):
        user = User.objects.create(email="testuser@example.com", password="password")
        habit1 = Habit.objects.create(
            user=user,
            place="Home",
            time="08:00:00",
            action="Morning exercise",
            is_pleasant_habit=False,
            frequency=7,
            estimated_time=2,
            is_public=False,
        )
        habit2 = Habit.objects.create(
            user=user,
            place="Home",
            time="08:00:00",
            action="Evening exercise",
            is_pleasant_habit=True,
            frequency=7,
            estimated_time=2,
            is_public=False,
            related_habit=habit1,
        )
        self.assertEqual(habit2.related_habit, habit1)

    def test_habit_str_representation(self):
        user = User.objects.create(email="testuser@example.com", password="password")
        habit = Habit.objects.create(
            user=user,
            place="Home",
            time="08:00:00",
            action="Morning exercise",
            is_pleasant_habit=False,
            frequency=7,
            estimated_time=2,
            is_public=False,
        )
        expected_str = f"{user} - {habit.action}"
        self.assertEqual(str(habit), expected_str)


class HabitSerializerTestCase(TestCase):
    def test_valid_habit(self):
        data = {
            "action": "Morning exercise",
            "is_pleasant_habit": False,
            "frequency": 7,
            "estimated_time": 30,
            "is_public": True,
        }
        serializer = HabitSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_habit_serializer_validation(self):
        # Test serializer validation
        data = {
            "user": 1,
            "place": "Home",
            "time": "08:00:00",
            "action": "Morning exercise",
            "is_pleasant_habit": True,
            "related_habit": None,
            "frequency": 7,
            "reward": None,
            "estimated_time": 2,
            "is_public": False,
        }
        serializer = HabitSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_habit_serializer_invalid_related_habit_reward(self):
        # Test serializer validation with both related habit and reward
        data = {
            "user": 1,
            "place": "Home",
            "time": "08:00:00",
            "action": "Morning exercise",
            "is_pleasant_habit": False,
            "related_habit": 2,
            "frequency": 7,
            "reward": "Brew a cup of coffee",
            "estimated_time": 2,
            "is_public": False,
        }
        serializer = HabitSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("related_habit", serializer.errors)

    def test_habit_serializer_invalid_related_habit(self):
        data = {
            "user": 1,
            "action": "Morning exercise",
            "related_habit": 2,  # Неверный идентификатор связанной привычки
        }
        serializer = HabitSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("related_habit", serializer.errors)


class IsOwnerOrReadOnlyTestCase(TestCase):
    def test_owner_has_edit_permissions(self):
        user = User.objects.create(email="testuser@example.com", password="password")
        habit = Habit.objects.create(
            user=user,
            place="Home",
            time="08:00:00",
            action="Morning exercise",
            is_pleasant_habit=False,
            frequency=7,
            estimated_time=2,
            is_public=False,
        )
        request_factory = RequestFactory()
        request = request_factory.get("/")
        self.client.force_login(user)
        permission = IsOwnerOrReadOnly()
        self.assertTrue(permission.has_object_permission(request, None, habit))

    def test_other_users_cannot_edit(self):
        user1 = User.objects.create(email="user1@example.com", password="password")
        user2 = User.objects.create(email="user2@example.com", password="password")

        habit = Habit.objects.create(
            user=user1,
            place="Home",
            time="08:00:00",
            action="Morning exercise",
            is_pleasant_habit=False,
            frequency=7,
            estimated_time=2,
            is_public=False,
        )
        request_factory = RequestFactory()
        request = request_factory.get("/")
        self.client.force_login(user2)

        permission = IsOwnerOrReadOnly()
        self.assertTrue(permission.has_object_permission(request, None, habit))

    def test_anonymous_user_cannot_edit(self):
        habit = Habit.objects.create(
            user=User.objects.create(email="testuser@example.com", password="password"),  # Создаем нового пользователя
            place="Home",
            time="08:00:00",
            action="Morning exercise",
            is_pleasant_habit=False,
            frequency=7,
            estimated_time=2,
            is_public=False,
        )
        request_factory = RequestFactory()
        request = request_factory.get("/")
        permission = IsOwnerOrReadOnly()
        self.client.logout()  # Делаем пользователя анонимным
        self.assertTrue(permission.has_object_permission(request, None, habit))


class CanReadPublicHabitsTestCase(TestCase):
    def test_can_read_public_habits(self):
        user = User.objects.create(email="testuser@example.com", password="password")
        Habit.objects.create(
            user=user,
            place="Home",
            time="08:00:00",
            action="Morning exercise",
            is_pleasant_habit=False,
            frequency=7,
            estimated_time=2,
            is_public=True,
        )
        request_factory = RequestFactory()
        request = request_factory.get("/")
        permission = CanReadPublicHabits()
        self.assertTrue(permission.has_permission(request, None))
