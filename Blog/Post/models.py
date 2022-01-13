from django.db import models
from django.db.models.fields import DateField

# Post Model
class BlogPost(models.Model):
    post_id = models.AutoField(primary_key = True)
    slug = models.CharField(max_length=50, default=None)
    Name = models.CharField(max_length=50, default=None)
    Category = models.CharField(max_length=50, default = None)
    author = models.CharField(max_length=50, default = None)
    content = models.TextField(default=None)
    date = DateField(default=None)
    img1 = models.ImageField(upload_to = "images")

    def __str__(self):
        return self.Name


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50, default=None)
    Suggestions = models.TextField(default = None)

    def __str__(self):
        return self.user_name