from django.db import models


# Create your models here.

class Dinosaurs(models.Model):
    width = models.IntegerField()
    height = models.IntegerField()
    is_live = models.BooleanField()


    @property
    def location(self):
        return self.width, self.height


class Robot(models.Model):
    width = models.IntegerField()
    height = models.IntegerField()
