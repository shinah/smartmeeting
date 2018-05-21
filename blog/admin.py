from django.contrib import admin
from .models import Post, Group, Vote, Document, Task, Chat

admin.site.register(Post)
admin.site.register(Group)
admin.site.register(Vote)
admin.site.register(Document)
admin.site.register(Task)
admin.site.register(Chat)
# Register your models here.
