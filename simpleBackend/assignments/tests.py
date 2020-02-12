from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import TaskView, TagView
from .serializers import TaskSerializer, TagSerializer
from rest_framework import routers

# Create your tests here.

# testing urls
class TestUrls(SimpleTestCase):

    def test_url_is_resolved(self):
        url = reverse('tasks')
        print(resolve(url))
