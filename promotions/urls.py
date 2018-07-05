from django.conf.urls import url

from .views import LandingPage

urlpatterns = [
    url(r'^$', LandingPage.as_view()),
]
