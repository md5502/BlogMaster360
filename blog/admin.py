from django.contrib import admin
from .models import Post, Category, Tag, Comment

# Custom Admin class for Post
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'publish_date', 'created_at', 'updated_at']
    search_fields = ['title', 'body', 'summary']
    list_filter = ['publish_date', 'owner']
    filter_horizontal = ('categories', 'tags')  # Many-to-Many fields will use this widget
    readonly_fields = ['created_at', 'updated_at']  # These fields will be read-only

# Custom Admin class for Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'created_at', 'updated_at']
    search_fields = ['title', 'meta_title']
    list_filter = ['created_at']
    readonly_fields = ['created_at', 'updated_at']

# Custom Admin class for Tag
class TagAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'created_at', 'updated_at']
    search_fields = ['title', 'meta_title']
    list_filter = ['created_at']
    readonly_fields = ['created_at', 'updated_at']

# Custom Admin class for Comment
class CommentAdmin(admin.ModelAdmin):
    list_display = ['owner', 'post', 'approved_comment', 'created_at', 'updated_at']
    search_fields = ['owner__username', 'post__title', 'body']  # Searchable by user and post
    list_filter = ['approved_comment', 'created_at']
    readonly_fields = ['created_at', 'updated_at']

# Registering models and custom Admin classes to the admin site
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)
