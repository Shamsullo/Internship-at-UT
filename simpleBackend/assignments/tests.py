from rest_framework import status

from rest_framework.test import APITestCase
from .models import Tag, Task


# Create your tests here.
class TaskTesting(APITestCase):

    url = 'http://localhost:8000/tasks/'
   
    def setUp(self):
        Task.objects.create(name='something', description='text', date_of_creation='2020-04-06'),
        Task.objects.create(name='something2', description='text2', date_of_creation='2020-05-06')

        
    def test_create_a_task(self):

        # print(resolve(url))
        data = {'name': 'Test',
                'description': 'Text',
                'date_of_creation': '2020-05-06',
                }
        
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.last().name, 'Test')
        self.assertEqual(str(Task.objects.last().date_of_creation), '2020-05-06')


    def test_get_all_tasks(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    
    def test_get_a_task(self):
        response = self.client.get(self.url + '1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)



class TagsTesting(APITestCase):
    
    url = 'http://localhost:8000/tags/'
   
    def setUp(self):
        Tag.objects.create(name='something', date_of_creation='2020-04-06'),
        Tag.objects.create(name='something2', date_of_creation='2020-05-06')

        
    def test_create_a_tag(self):

        data = {'name': 'Test1',
                'date_of_creation': '2020-05-06',
                }
        print(data)
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tags.objects.last().name, 'Test1')
        self.assertEqual(str(Tags.objects.last().date_of_creation), '2020-05-06')


    def test_get_all_tags(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    
    def test_get_a_tag(self):
        response = self.client.get(self.url + '1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)




