from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length = 120, null = False, blank=False)
    date_of_creation = models.DateField(editable = True, blank = False)

    def __str__(self):
        return self.name



class Task(models.Model):
    name = models.CharField(max_length = 120, null = False, blank=False)
    description = models.TextField(null = False, blank=False)
    date_of_creation = models.DateField(editable = True, blank = False)
    tags = models.ManyToManyField(Tag, related_name='tasks')

    def __str__(self):
        return self.name