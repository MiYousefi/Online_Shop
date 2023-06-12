from django.urls import path

from . views import HomePageView, AboutUsPageView

urlpatterns = [
    path('aboutus', AboutUsPageView.as_view(), name='aboutus'),

]
