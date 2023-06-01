from django.urls import path
from . import views

urlpatterns = [
    # Путь к сериям
    path('series/', views.series_view, name='series'),
    # Путь к статусам серий
    path('series/status/', views.series_status_view, name='series-status'),
    # Путь к главам
    path('chapters/', views.chapters_view, name='chapters'),
    # Путь к статусам глав
    path('chapters/status/', views.chapters_status_view, name='chapters-status'),
]