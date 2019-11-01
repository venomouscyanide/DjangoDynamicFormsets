from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

from django_dynamic_formsets.users.forms import UserChangeForm, UserCreationForm
from django_dynamic_formsets.users.models import Example2Model

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (("User", {"fields": ("name",)}),) + auth_admin.UserAdmin.fieldsets
    list_display = ["username", "name", "is_superuser"]
    search_fields = ["name"]


@admin.register(Example2Model)
class Example2Admin(admin.ModelAdmin):
    list_display = ('name', 'email', 'address', 'phone_number', 'created_on', 'updated_at')
    search_fields = ['address', 'name']
    list_filter = ('created_on', 'updated_at')
