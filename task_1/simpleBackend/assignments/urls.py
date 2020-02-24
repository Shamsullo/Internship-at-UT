
from django.urls import path, include
from . import views
from rest_framework import routers



router = routers.DefaultRouter()
router.register('tasks', views.TaskView, basename='tasks')
router.register('tags', views.TagView, basename='tags')


urlpatterns = [
    path(r'', include(router.urls)),

    # path('api/instances/', views.InstanceList.as_view(), name="instances"),
    # path('', include('assignments.urls'))
]   