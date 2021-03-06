from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import ImageField
from users.models import Profile

class Post(models.Model):
    caption = models.TextField()
    image = models.ImageField(upload_to = 'images/')
    date_posted = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name= 'likes', blank = True)
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    classmethod
    def get_all_images(cls):
        images = cls.objects.all()
        return images
        
    def total_likes(self):
       self.likes.count()

    def save_post(self):
        self.save()
    
    def delete_post(self):
        self.delete()

    
    
    def __str__(self):
        return self.caption


    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Comment(models.Model):
    text = models.TextField()
    photo = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)


    def __str__(self):
        return self.profile


    