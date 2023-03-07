from django.contrib import admin

# Register your models here.
from .models import Profile,skill,todo ,Exercise

admin.site.register(Profile)
admin.site.register(skill)
admin.site.register(todo)
admin.site.register(Exercise)