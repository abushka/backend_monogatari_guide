from django.urls import path
from . import views

urlpatterns = [
    # Путь к сериям
    path('series/', views.series_view, name='series'),
    # Путь к статусам серий
    path('series/status/', views.series_status_view, name='series-status'),
    # Путь к сезонам
    path('seasons/', views.seasons_view, name='seasons'),
    # Путь к статусам сезонов
    path('seasons/status/', views.seasons_status_view, name='seasons-status'),
    # Сохранение статуса для сезонов
    path('seasons/status/change/', views.seasons_save_status_view, name='seasons-status-change'),
    # Путь к главам
    path('chapters/', views.chapters_view, name='chapters'),
    # Путь к статусам глав
    path('chapters/status/', views.chapters_status_view, name='chapters-status'),
    # Путь к томам
    path('volumes/', views.volumes_view, name='volumes'),
    # Путь к статусам томов
    path('volumes/status/', views.volumes_status_view, name='volumes-status'),
]