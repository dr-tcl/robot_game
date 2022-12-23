from django.contrib import admin
from .models import Robot, Dinosaurs
# Register your models here.

@admin.register(Robot)
class RobotAdmin(admin.ModelAdmin):
    pass

@admin.register(Dinosaurs)
class DinosaursAdmin(admin.ModelAdmin):
    pass