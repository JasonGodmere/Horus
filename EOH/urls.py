

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from EOH import views

urlpatterns = [
    path('initnode/', views.InitNode.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)