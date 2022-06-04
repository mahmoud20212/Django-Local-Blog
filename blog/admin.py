from django.contrib import admin
from .models import *

admin.site.register(BlogAuthor)
admin.site.register(BlogComment)
# Register your models here.

class BlogCommentsInline(admin.TabularInline):
    model = BlogComment
    max_num = 0

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    """
    Administration object for Blog models. 
    Defines:
     - fields to be displayed in list view (list_display)
     - orders fields in detail view (fields), grouping the date fields horizontally
     - adds inline addition of blog comments in blog view (inlines)
    """
    list_display = ('name', 'author', 'post_date')
    inlines = [BlogCommentsInline]