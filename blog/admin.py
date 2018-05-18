from django.contrib import admin
from .models import Post, Group, Comment, Vote, Document

admin.site.register(Post)
admin.site.register(Group)
admin.site.register(Comment)
admin.site.register(Vote)
admin.site.register(Document)
#admin.site.register(doVote)
# Register your models here.
