from django.urls import path
from . import views

urlpatterns=[
    path('findBestCandidates/', views.handle_candidates_query)
]