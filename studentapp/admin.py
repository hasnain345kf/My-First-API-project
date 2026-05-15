from django.contrib import admin
from .models import student
admin.site.register(student)
class studentadmin(admin.ModelAdmin):
    model=student
    search_list=['name','s_id']
