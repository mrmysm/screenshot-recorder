from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (ScreenshotsList, ScreenshotDetails)
from apps.screenshots import views

urlpatterns = [
    path('screenshots/', ScreenshotsList.as_view()),
    path('screenshots/<int:pk>/', ScreenshotDetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
