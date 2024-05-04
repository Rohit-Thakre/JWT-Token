
# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from account import models



# class UserAdmin(BaseUserAdmin):
 
#     list_display = ["email", "name", "is_admin"]
#     list_filter = ["is_admin","name"]

#     # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
#     # overrides get_fieldsets to use this attribute when creating a user.
#     add_fieldsets = [
#         (
#             None,
#             {
#                 "classes": ["wide"],
#                 "fields": ["email", "name", "password1", "password2","is_active","is_admin"],
#             },
#         ),
#     ]
#     search_fields = ["email","name"]
#     ordering = ["email"]
#     filter_horizontal = []


# admin.site.register(models.CustomUser, UserAdmin)


from django.contrib import admin
from account import models

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["email", "name", "is_admin"]
    list_filter = ["is_admin","name"]

    class Meta: 
        model = models.CustomUser

admin.site.register(models.CustomUser, CustomUserAdmin)