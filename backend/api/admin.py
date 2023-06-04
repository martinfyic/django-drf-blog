from django.contrib import admin
from .models import Blog, Category

# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ('date_created', 'date_updated')
    list_display = ('title', 'date_created', 'date_updated', 'feature')
    date_hierarchy = 'date_created'


admin.site.register(Blog, BlogAdmin)


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('date_created', 'date_updated')
    list_display = ('title', 'date_created', 'date_updated')
    date_hierarchy = 'date_created'


admin.site.register(Category, CategoryAdmin)
