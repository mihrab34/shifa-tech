from django.urls import path

from .views import ReviewListView, ReviewDetailView

urlpatterns = [
    path('', ReviewListView.as_view(), name='review_list'),
    path('<uuid:pk>', ReviewDetailView.as_view(), name='review_detail')
]