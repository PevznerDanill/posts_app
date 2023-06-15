from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=64, verbose_name='title')
    description = models.CharField(max_length=128, verbose_name='description')
    content = models.TextField(verbose_name='content')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created_at')

    class Meta:
        verbose_name_plural = 'posts'
        verbose_name = 'post'
        ordering = '-created_at',

    def __str__(self) -> str:
        """
        Returns the title of the post.
        """
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(to=User, verbose_name='user', related_name='comments', on_delete=models.CASCADE)
    content = models.TextField(verbose_name='content')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created_at')
    post = models.ForeignKey(to=Post, verbose_name='post', related_name='comments', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'comments'
        verbose_name = 'comment'
        ordering = '-created_at',
