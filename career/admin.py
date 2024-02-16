from django.contrib import admin

# Register your models here.
from .models import Career

class CareerAdmin(admin.ModelAdmin):
    list_display = ['short_name', 'level']
    list_filter = ['level']

admin.site.register(Career, CareerAdmin)