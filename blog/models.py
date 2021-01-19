from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

from taggit.managers import TaggableManager
# Create your models here.
from UserRegistration.models import User

class Category(models.Model):
    category_name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True, null=True)

    class Meta:
        verbose_name = ' category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name

    def post_count(self):
        return self.posts.all().count()

class Post(models.Model):

    title = models.CharField(max_length=50)
    content = models.TextField()
    detail_content = models.TextField()
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    # tags
    category = models.ForeignKey(Category  ,null=True, on_delete=models.SET_NULL, related_name='posts')
    created  = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(blank=True, null=True)

    tags = TaggableManager(blank=True)
# 'taggit', needs to paste in settings, Inatall App

    class Meta:
        verbose_name = ' post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.title



    def comment_count(self):
        return self.comments.all().count()









class Comment(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE,related_name='commentuser')
    post = models.ForeignKey(Post , on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return str(self.post)


class Newsletter(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
