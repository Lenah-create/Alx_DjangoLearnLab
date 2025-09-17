# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ["username", "email", "date_of_birth", "is_staff", "is_active"]
    fieldsets = UserAdmin.fieldsets + (
<<<<<<< HEAD:advanced_features_and_security/users/admin.py
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )


=======
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

>>>>>>> e9111a16da3f1b89bf08c90f5d93b63769ffb2ec:users/admin.py
admin.site.register(CustomUser, CustomUserAdmin)
