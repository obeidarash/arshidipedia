from django.db import models
from accounting.models import Contact, Company




class Post(models.Model):
    title = models.CharField(max_length=52, blank=True, null=True)


class Comment(models.Model):
    blog = models.ForeignKey(to=Post, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    is_published = models.BooleanField(default=False)
    added_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Blog Comment'
        verbose_name_plural = 'Blog Comments'

    def __str__(self):
        return f"{self.blog.title} - {self.content}"
