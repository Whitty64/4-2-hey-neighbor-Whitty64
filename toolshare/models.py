from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


User = get_user_model()

BOOL_CHOICES = ((True, 'Available'), (False, 'Not Available'))


class Bike(models.Model):
    bike_name = models.CharField(max_length=250)
    bike_type = models.CharField(max_length=250)
    description = models.TextField()
    model_pic = models.CharField(max_length=250)
    guide_pic = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    available = models.BooleanField(choices=BOOL_CHOICES, default=True)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.bike_name[:20]

    def get_absolute_url(self):
        return reverse('home')
