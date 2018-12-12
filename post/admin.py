from django.contrib import admin

from post import models

class PostAdmin(admin.ModelAdmin):
    list_display = [
        'author',
        'title',
        'created_date',
        'category'
    ]

admin.site.register(models.Post, PostAdmin)
admin.site.register(models.PostCategory)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'body')

admin.site.register(models.Comment, CommentAdmin)
