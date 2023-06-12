from django.contrib import admin
from .models import Season, Serie, Volume, Chapter, SeasonStatus, SerieStatus, VolumeStatus, ChapterStatus, \
                    SerieImage, SeasonImage, VolumeImage, ChapterImage
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html

# Серии
class SerieStatusInline(admin.TabularInline):
    model = SerieStatus
    extra = 0

class SerieImagesInline(admin.StackedInline):
    model = SerieImage
    extra = 0

    readonly_fields = ("display_image",)

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="200" />', obj.image.url)
        else:
            return None

    display_image.short_description = 'Image'

class SerieAdmin(admin.ModelAdmin):
    list_display = ('name_ru', 'number', 'name_en', 'name_jp')
    inlines = [SerieImagesInline, SerieStatusInline]
    ordering = ['number']

    fieldsets = (
        (None, {"fields": ("number", "anime_release_view_number", "ranobe_release_number", "chronological_view_number",
                            "name_ru", "name_en", "name_jp", "url", "description_ru", "description_en", "description_jp",
                            "image", "season")}),
        (
            _("Image"),
            {
                "fields": ("image_preview",),
            },
        ),
    )
    readonly_fields = ("image_preview",)

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        else:
            return None

    display_image.short_description = 'Image'

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="200" />', obj.image.url)
        else:
            return None

    image_preview.short_description = 'Image Preview'


# Сезоны
class SerieInline(admin.TabularInline):
    model = Serie
    extra = 0

class SeasonStatusInline(admin.TabularInline):
    model = SeasonStatus
    extra = 0

class SeasonImagesInline(admin.StackedInline):
    model = SeasonImage
    extra = 0

    readonly_fields = ("display_image",)

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="200" />', obj.image.url)
        else:
            return None

    display_image.short_description = 'Image'

@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ('name_ru', 'number', 'name_en', 'name_jp')
    inlines = [SeasonImagesInline, SerieInline, SeasonStatusInline]
    ordering = ['number']

    fieldsets = (
        (None, {"fields": ("number", "anime_release_view_number", "ranobe_release_number", "chronological_view_number",
                            "name_ru", "name_en", "name_jp", "url", "description_ru", "description_en", "description_jp",
                            "image")}),
        (
            _("Image"),
            {
                "fields": ("image_preview",),
            },
        ),
    )
    readonly_fields = ("image_preview",)

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        else:
            return None

    display_image.short_description = 'Image'

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="200" />', obj.image.url)
        else:
            return None

    image_preview.short_description = 'Image Preview'



# Томы
class ChapterInline(admin.TabularInline):
    model = Chapter
    extra = 0

class VolumeStatusInline(admin.TabularInline):
    model = VolumeStatus
    extra = 0

class VolumeImagesInline(admin.StackedInline):
    model = VolumeImage
    extra = 0

    readonly_fields = ("display_image",)

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="200" />', obj.image.url)
        else:
            return None

    display_image.short_description = 'Image'

@admin.register(Volume)
class VolumeAdmin(admin.ModelAdmin):
    list_display = ('name_ru', 'number', 'name_en', 'name_jp')
    inlines = [VolumeImagesInline ,ChapterInline, VolumeStatusInline]
    ordering = ['number']

    fieldsets = (
        (None, {"fields": ("number", "name_ru", "name_en", "name_jp", "url", "description_ru", "description_en", "description_jp", "image",)}),
        (
            _("Image"),
            {
                "fields": ("image_preview",),
            },
        ),
    )
    readonly_fields = ("image_preview",)

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        else:
            return None

    display_image.short_description = 'Image'

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="200" />', obj.image.url)
        else:
            return None

    image_preview.short_description = 'Image Preview'



# Главы
class ChapterStatusInline(admin.TabularInline):
    model = ChapterStatus
    extra = 0

class ChapterImagesInline(admin.StackedInline):
    model = ChapterImage
    extra = 0

    readonly_fields = ("display_image",)

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="200" />', obj.image.url)
        else:
            return None

    display_image.short_description = 'Image'

class ChapterAdmin(admin.ModelAdmin):
    list_display = ('name_ru', 'number', 'name_en', 'name_jp')
    inlines = [ChapterImagesInline, ChapterStatusInline]
    ordering = ['number']

    fieldsets = (
        (None, {"fields": ("number", "name_ru", "name_en", "name_jp", "url", "description_ru", "description_en", "description_jp", "image", "volume")}),
        (
            _("Image"),
            {
                "fields": ("image_preview",),
            },
        ),
    )
    readonly_fields = ("image_preview",)

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        else:
            return None

    display_image.short_description = 'Image'

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="200" />', obj.image.url)
        else:
            return None

    image_preview.short_description = 'Image Preview'


admin.site.register(Serie, SerieAdmin)
admin.site.register(Chapter, ChapterAdmin)
