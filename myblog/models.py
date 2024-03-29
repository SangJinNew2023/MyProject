from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PostModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True) #auto_now_add=True:Automatically add date

    class Meta:
        ordering = ('-date_created',) # The results in reverse order

    def comment_count(self):
        return self.myblogcomment_set.all().count()

    def comments(self):
        return self.myblogcomment_set.all()

    def __str__(self):
        return self.title


class MyBlogComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content