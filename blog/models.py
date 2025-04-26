from django.db import models
from django.contrib.auth.models import User
from categorys.models import Categorys as Category


class Blog(models.Model):
    title = models.CharField(max_length=500, blank=False, null=False)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    is_sticky = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    poster = models.TextField()
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return '%s %s' % (self.blog.id, self.text)
