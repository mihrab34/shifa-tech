from django.contrib import admin

from .models import Review

# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'likes', 'dislikes', 'date_created')

admin.site.register(Review, ReviewAdmin)