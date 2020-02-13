from rest_framework import serializers
from .models import Task, Tag

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    tags = serializers.StringRelatedField(many=True, required=False)
    class Meta:
        model = Task
        fields = ('id', 'name', 'description', 'date_of_creation', 'tags')


class TagSerializer(serializers.ModelSerializer):

    tasks = serializers.StringRelatedField(many=True, required=False)

    class Meta:
        model = Tag
        fields = ('id', 'name', 'date_of_creation', 'tasks')
       

    