from django.contrib import admin
from . import models

@admin.register(models.Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = (
        'Music_name',
        'Singer_name',
        'Grade',
    )
