from django.contrib import admin
from .models import *

# Register your models here.
""" 
class QuestionAdmin(admin.ModelAdmin):
    fields=['top','letter']

"""
class QuestionAdmin(admin.ModelAdmin):
    fieldsets=[
        (None, {"fields":["top"]}),
        ("Date information",{"fields":["letter"]}),
    ]
admin.site.register(Result,QuestionAdmin)