from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Review

# Create your views here.

class ReviewListView(ListView):
    model = Review
    context_object_name = 'review_list'
    template_name = 'blog/review_list.html'


class ReviewDetailView(DetailView):
    model = Review
    context_object_name = 'review'
    template_name = 'blog/review_detail.html'