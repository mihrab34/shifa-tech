import uuid
from django.db import models
from django.urls import reverse

# Create your models here.
class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200, blank=True, null=True)
    post = models.TextField(blank=True, null=True)
    date_created = models.DateField(auto_now_add=True)
    likes = models.IntegerField(blank=True, null=True)
    dislikes = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ['-date_created', 'title']

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('review_detail', args=[str(self.id)])
    