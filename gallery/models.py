from django.db import models
from django.contrib import admin


class Blog(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    timestamp = models.DateTimeField()
    class Meta:
        ordering = ('-timestamp',)

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','timestamp')

admin.site.register(Blog,BlogPostAdmin,)
