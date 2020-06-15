from django.contrib import admin
from .models import Family, Child, Tree, Images
# Register your models here.

admin.site.register(Family)
admin.site.register(Child)
admin.site.register(Tree)
admin.site.register(Images)

class FamilyAdmin(admin.ModelAdmin):
    list_display = ['name']

class ChildAdmin(admin.ModelAdmin):
    list_display = ['parentid']

class TreeAdmin(admin.ModelAdmin):
    list_display = ['familyname']

class ImagesAdmin(admin.ModelAdmin):
    list_display = ['globalid']