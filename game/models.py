from django.db import models


# Create your models here.

class Dinosaurs(models.Model):
    width = models.IntegerField()
    height = models.IntegerField()
    is_live = models.BooleanField(default=True)

    @property
    def location(self):
        return self.width, self.height

    def __str__(self):
        return str(self.location)

class Robot(models.Model):
    width = models.IntegerField()
    height = models.IntegerField()

    def __str__(self):
        return f"({self.width}, {self.height})"
