from django.contrib import admin
from .models import Post, Group, Comment, Vote, Document, Task

admin.site.register(Post)
admin.site.register(Group)
admin.site.register(Vote)
admin.site.register(Document)
admin.site.register(Task)
# Register your models here.
