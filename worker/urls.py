from django.urls import path
from . import views

urlpatterns = [
    # Путь к сериям
    path('series/', views.series_view, name='series'),
    # Путь к статусам серий
    path('series/status/', views.series_status_view, name='series-status'),
    # Сохранение статуса для серий
    path('series/status/change/', views.series_save_status_view, name='series-status-change'),
    # Сезоны и серии по дате выхода (anime_release_view_number)
    path('series/anime-release/', views.series_anime_realease_view, name='series_anime_realease'),
    # Сезоны и серии по Хронологии (chronological_view_number)
    path('series/chronological/', views.series_chronological, name='series_chronological'),
    # Сезоны и серии по Ранобэ (ranobe_release_number)
    path('series/ranobe/', views.series_ranobe_release, name='series_series_ranobe'),
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
    # Сохранение статуса для глав
    path('chapters/status/change/', views.chapters_save_status_view, name='chapters-status-change'),
    # Путь к томам
    path('volumes/', views.volumes_view, name='volumes'),
    # Путь к статусам томов
    path('volumes/status/', views.volumes_status_view, name='volumes-status'),
    # Сохранение статуса для томов
    path('volumes/status/change/', views.volumes_save_status_view, name='volumes-status-change'),
]