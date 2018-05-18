from django.contrib import admin
from .models import Post, Group, Vote, doVote, Task

admin.site.register(Post)
admin.site.register(Group)
admin.site.register(Vote)
admin.site.register(doVote)
admin.site.register(Task)
# Register your models here.
