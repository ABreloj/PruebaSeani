from django.contrib import admin
from .models import Question, Module
# Register your models here.
admin.site.register(Module)
admin.site.register(Question)