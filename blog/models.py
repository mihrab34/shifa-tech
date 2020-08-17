import uuid
from django.db import models
from django.urls import reverse

from djrichtextfield.models import RichTextField

from accounts.models import CustomUser

# Create your models here.
class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200, blank=True, null=True)
    post = models.TextField(blank=True, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reviews')
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_updated', 'title']

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('review_detail', args=[str(self.id)])
    