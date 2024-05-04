from django.contrib import admin
from account import models

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["email", "name", "is_admin"]
    list_filter = ["is_admin","name"]

    class Meta: 
        model = models.CustomUser

admin.site.register(models.CustomUser, CustomUserAdmin)