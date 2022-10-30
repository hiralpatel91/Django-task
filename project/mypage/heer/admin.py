from django.contrib import admin
from .models import Add

# Register your models here.

@admin.register(Add)
class AddAdmin(admin.ModelAdmin):
    list_display = ['name','branch','language','field','technical_language']
    
 