from django.db import models
from users.models import User


class Palette(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='palettes')


class Color(models.Model):
    palette = models.ForeignKey(Palette, on_delete=models.PROTECT, related_name='colors')
    hex = models.CharField(max_length=32)
    name = models.CharField(max_length=255)
