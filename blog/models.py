from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50, verbose_name="Title", unique=True )
    meta_title = models.CharField(max_length=100, verbose_name="Meta Title", unique=True, null=True, blank=True )
    body = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    categories = models.ManyToManyField("Category", blank=True)
    tags = models.ManyToManyField("Tag", blank=True)
    summary = models.CharField(max_length=300, null=True, blank=True)
    image = models.ImageField("Post image", default="default.png", null=True, blank=True, upload_to="uploads/")
    slug =AutoSlugField(max_length=100, populate_from="title", unique_with=["publish_date"])
    publish_date = models.DateField(auto_now_add=True)

    created_at = models.DateTimeField(verbose_name="Created At", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated At", auto_now=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=70, verbose_name="name", unique=True )
    slug =AutoSlugField(max_length=100, populate_from="title", unique_with=["created_at"])
    meta_title = models.CharField(max_length=100, verbose_name="Meta Title", unique=True )
    body = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(verbose_name="Created At", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated At", auto_now=True)


    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length=70, verbose_name="name", unique=True )
    slug =AutoSlugField(max_length=100, populate_from="title", unique_with=["created_at"])
    meta_title = models.CharField(max_length=100, verbose_name="title", unique=True )
    body = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(verbose_name="Created At", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated At", auto_now=True)


    def __str__(self):
        return self.title



class Comment(models.Model):
    body = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    created_at = models.DateTimeField(verbose_name="Created At", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated At", auto_now=True)

    approved_comment = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.owner}- {self.pk}"

    def approve(self):
        self.approved_comment = True
        self.save()



