from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


User = get_user_model()

class Tool(models.Model):
    toolname = models.CharField(max_length=250)
    type_of_tool = models.CharField(max_length=250)
    description = models.TextField()
    model_pic = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )




    def __str__(self):
        return self.toolname[:20]

    def get_absolute_url(self):
        return reverse('home')
