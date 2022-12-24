from django.contrib import admin
from .models import Robot, Dinosaurs


# Register your models here.

@admin.register(Robot)
class RobotAdmin(admin.ModelAdmin):
    list_display = ["width", "height"]


@admin.register(Dinosaurs)
class DinosaursAdmin(admin.ModelAdmin):
    list_display = ["width", "height", "is_live"]
