from django.test import TestCase
from django.db import IntegrityError
from blog.models import *
class UserTest(TestCase):

   def test_creacion_user(self):
       user = User(first_name="Pepito", last_name="Perez", username="PepitoPerez3110", email="pperez@example.com")
       user.save()

       self.assertEqual(User.objects.count(), 1)
       self.assertEqual(user.first_name, "Pepito")
       self.assertEqual(user.last_name, "Perez")
       self.assertEqual(user.username, "PepitoPerez3110")
       self.assertEqual(user.email, "pperez@example.com")