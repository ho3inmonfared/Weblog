from django.contrib import admin
from . import models
from django.utils.text import Truncator


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('title','short_description','author','created_at','status', )
    list_filter=('created_at','status', )
    search_fields=('title','short_description', )
    
    def short_description(self,obj):
        return Truncator(obj.description).words(5)
