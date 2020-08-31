from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#this auto_now_add will create the date_posted to the date it was createdif we remove 'add' it means will change every time we update it
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) # this is a function but we dont want it to be executes as a function
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title