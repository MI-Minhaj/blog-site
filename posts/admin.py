from django.contrib import admin
from posts.models import Post
from posts.models import Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ["id","title","publish_date"]

class CommentAdmin(admin.ModelAdmin):
    list_display = ["id","content"]

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
