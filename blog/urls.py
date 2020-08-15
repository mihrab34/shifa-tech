from django.urls import path

from .views import ReviewListView, ReviewDetailView, ReviewCreateView, like, dislike

urlpatterns = [
    path('', ReviewListView.as_view(), name='review_list'),
    path('<uuid:pk>', ReviewDetailView.as_view(), name='review_detail'),
    path('create/', ReviewCreateView.as_view(), name='review_create'),
    path('like/<uuid:id>', like, name='like'),
    path('dislike/<uuid:id>', dislike, name='dislike')
]