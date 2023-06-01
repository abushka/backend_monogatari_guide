from django.contrib import admin
from .models import Season, Serie, Volume, Chapter, ChapterStatus, SeasonStatus, SerieStatus, VolumeStatus

# Серии
class SerieStatusInline(admin.TabularInline):
    model = SerieStatus
    extra = 0

class SerieAdmin(admin.ModelAdmin):
    list_display = ('name_ru', 'number', 'name_en', 'name_jp')
    inlines = [SerieStatusInline]
    ordering = ['number']

# Сезоны
class SerieInline(admin.TabularInline):
    model = Serie
    extra = 0

class SeasonStatusInline(admin.TabularInline):
    model = SeasonStatus
    extra = 0

@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ('name_ru', 'number', 'name_en', 'name_jp')
    inlines = [SerieInline, SeasonStatusInline]
    ordering = ['number']


# Главы
class ChapterStatusInline(admin.TabularInline):
    model = ChapterStatus
    extra = 0

class ChapterAdmin(admin.ModelAdmin):
    list_display = ('name_ru', 'number', 'name_en', 'name_jp')
    inlines = [ChapterStatusInline]
    ordering = ['number']

# Томы
class ChapterInline(admin.TabularInline):
    model = Chapter
    extra = 0

class VolumeStatusInline(admin.TabularInline):
    model = VolumeStatus
    extra = 0

@admin.register(Volume)
class VolumeAdmin(admin.ModelAdmin):
    list_display = ('name_ru', 'number', 'name_en', 'name_jp')
    inlines = [ChapterInline, VolumeStatusInline]
    ordering = ['number']


admin.site.register(Serie, SerieAdmin)
admin.site.register(Chapter, ChapterAdmin)
