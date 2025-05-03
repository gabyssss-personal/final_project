from django.db import models
from django.contrib.auth.models import User


# create a model to represent each recipe

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    cooking_time = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title