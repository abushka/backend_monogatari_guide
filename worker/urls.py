from django.urls import path
from . import views

urlpatterns = [
    # Путь к сериям
    path('series/', views.series_view, name='series'),
    # Путь к статусам серий
    path('series/status/', views.series_status_view, name='series-status'),
]