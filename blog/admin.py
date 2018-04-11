from django.contrib import admin
from .models import Post, Group, Comment, User_belong

admin.site.register(Post)
admin.site.register(Group)
admin.site.register(Comment)
admin.site.register(User_belong)
# Register your models here.
