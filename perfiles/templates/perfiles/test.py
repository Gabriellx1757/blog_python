from django.test import TestCase
from django.db import IntegrityError
from blog.models import *
class UserTest(TestCase):

   def test_creacion_user(self):
       user = User(first_name="juan", last_name="ramon", username="juanramon123", email="jramon@example.com")
       user.save()

       self.assertEqual(User.objects.count(), 1)
       self.assertEqual(user.first_name, "juan")
       self.assertEqual(user.last_name, "ramon")
       self.assertEqual(user.username, "juanramon123")
       self.assertEqual(user.email, "jramon@example.com")