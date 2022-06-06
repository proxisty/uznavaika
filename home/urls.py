from django.urls import path
from .views import HomeView, FeedBackView, SuccessView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact/', FeedBackView.as_view(), name='contact'),
    path('contact/success/', SuccessView.as_view(), name='success')
]