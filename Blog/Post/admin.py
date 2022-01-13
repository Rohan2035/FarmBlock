from Post.models import BlogPost, Contact
from django.contrib import admin

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(Contact)

# @admin.register(BlogPost)
# class PostAdmin(admin.ModelAdmin):
#     class Media:
#         js = ('tiny.js',)

