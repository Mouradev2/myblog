from django.contrib import admin
from blog_app.models import Post, Comment

# Code v 1
# admin.site.register(Post)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "author", "publish", "status"]
    list_filter = ["status", "created", "publish", "author"]
    search_fields = ["title", "body"]
    prepopulated_fields = {
        "slug": ("title",)
    }  # slug field is filled in automatically by the input of title field
    raw_id_fields = ["author"]  # author field is now displayed with a lookup widget
    date_hierarchy = "publish"
    ordering = ["status", "publish"]

# admin.site.register(Comment) # ME
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'post', 'created', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'email', 'body']