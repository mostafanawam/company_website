from django.contrib import admin
from .views import *
# Register your models here.


class PostsAdmin(admin.ModelAdmin):  
    list_display = (
        "id",
        "title",
        "author",
        'created_at'
    )
admin.site.register(Post,PostsAdmin)


class CommentAdmin(admin.ModelAdmin):  
    list_display = (
        "id",
        "post",
        "author",
        'created_at'
    )
admin.site.register(Comment,CommentAdmin)



class TagAdmin(admin.ModelAdmin):  
    list_display = (
        "id",
        "name",
    )
admin.site.register(Tag,TagAdmin)

