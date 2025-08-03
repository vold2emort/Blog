from django.contrib import admin
from .models import Post, Author, Tag, Comment

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_filter = ("author", "tags", "date")
    list_display = ('title', 'date', 'author')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user_name', 'user_email')
    search_fields = ('user_name', 'user_email', 'text')
    list_filter = ('post',)


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)