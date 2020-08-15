from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView

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


class ReviewCreateView(CreateView):
    model = Review
    fields = ['title', 'post']
    template_name = 'blog/review_create.html'
    success_url = '/blog/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


def like(request, id):
    review = Review.objects.get(id=id)
    review.likes += 1
    review.save()
    return HttpResponseRedirect(review.get_absolute_url())

def dislike(request, id):
    review = Review.objects.get(id=id)
    review.dislikes += 1
    review.save()
    return HttpResponseRedirect(review.get_absolute_url())
