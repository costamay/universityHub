from django.db import models
from django.urls import reverse
from django.conf import settings


CATEGORIES = [
    ('WEB', 'WEB'),
    ('MOBILE', 'MOBILE'),
    ('DESIGN', 'DESIGN'),
]

class Author(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile')
    
    def __str__(self):
        return self.user.username
    
class ProjectPost(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=100, default=False)
    project_picture = models.ImageField(upload_to='projects', default=False)
    project_description = models.TextField(max_length=300, default=False)
    project_category = models.CharField(max_length=6, choices=CATEGORIES)
    project_url = models.URLField(max_length=200, help_text='enter project live link')
    timestamp = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.project_name
    
    class Meta:
        ordering = ['-timestamp']
        
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={
            'id': self.pk
        })
        
    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')
        
    @property
    def comment_count(self):
        return Comment.objects.filter(project_posted=self).count()
    
class Comment(models.Model):
    project_posted = models.ForeignKey(ProjectPost, related_name='comments', on_delete=models.CASCADE)
    description = models.TextField(max_length=200, default=False)
    timestamp = models.DateField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
    
    
    
