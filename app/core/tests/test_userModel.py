from django.test import TestCase
from django.contrib.auth import get_user_model

class TestCreatUser(TestCase):
    def test_create_user(self):
        email = 'test@gmail.com'
        password = '1234'
        user = get_user_model().objects.create_user(
        email=email,
        Password = password
        )
		
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        
        
    def test_create_user_norm(self):
       email = 'tes1t@GMAIL.COM'
       password = '1234'
       user = get_user_model().objects.create_user(
       email=email,
	   Password = password
        )
		
       self.assertEqual(user.email, email.lower())
        
       
    def test_create_value_error(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,"123")


    def test_create_superuser(self):
        user = get_user_model().objects.create_superuser(
            "test@gmail.com",
            "12345")
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
        
            


		