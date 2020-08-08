from django.urls import path, include

from .views import HomePageView, ContactPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('blog/', include('blog.urls'))
]