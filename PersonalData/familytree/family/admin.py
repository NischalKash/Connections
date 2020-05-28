from django.contrib import admin
from .models import Family, Child
# Register your models here.

admin.site.register(Family)
admin.site.register(Child)

class FamilyAdmin(admin.ModelAdmin):
    list_display = ['name']

class ChildAdmin(admin.ModelAdmin):
    list_display = ['parentid']