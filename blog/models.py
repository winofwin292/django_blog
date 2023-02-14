from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User

# Create your models here.

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return '%s' % self.title

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    title_img = models.ImageField()
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = RichTextUploadingField(config_name="custom_ckeditor")
    posted = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=0)

    def __unicode__(self):
        return '%s' % self.title

    class Meta:
        ordering = ['-posted']

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    post_at = models.DateTimeField(auto_now_add=True)
    body = models.TextField()


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    time_stamp = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    def __str__(self):
        return self.name + ' - ' + self.email
