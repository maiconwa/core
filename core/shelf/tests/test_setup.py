from rest_framework.test import APITestCase
from django.urls import reverse

class TestSetup(APITestCase):
    
    def setUp(self):
        return super().setUp()
    
    def tearDown(self) -> None:
        return super().tearDown()
    
