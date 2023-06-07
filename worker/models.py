from django.db import models
from auth_user.models import CustomUser

class Season(models.Model):
    number = models.IntegerField(blank=True, null=True)
    anime_release_view_number = models.IntegerField(blank=True, null=True)
    ranobe_release_number = models.IntegerField(blank=True, null=True)
    chronological_view_number = models.IntegerField(blank=True, null=True)

    name_ru = models.CharField(max_length=100, verbose_name='Название (русский)', blank=True, null=True)
    name_en = models.CharField(max_length=100, verbose_name='Название (английский)', blank=True, null=True)
    name_jp = models.CharField(max_length=100, verbose_name='Название (японский)', blank=True, null=True)
    users = models.ManyToManyField(CustomUser, through='SeasonStatus')

    url = models.CharField(max_length=250, verbose_name='Ссылка', blank=True, null=True)

    description_ru = models.TextField(verbose_name='Описание (русский)', blank=True, null=True)
    description_en = models.TextField(verbose_name='Описание (английский)', blank=True, null=True)
    description_jp = models.TextField(verbose_name='Описание (японский)', blank=True, null=True)

    image_file_url =  models.TextField(verbose_name='Ссылка на изображение', blank=True, null=True)

    def __str__(self):
        return self.name_ru


class SeasonStatus(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    STATUS_CHOICES = (
        ('not-watched', 'Не просмотрено'),
        ('watching', 'Смотрю'),
        ('watched', 'Просмотрено'),
        ('to-watch', 'Буду смотреть'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not-watched')
    favorite = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.season.name_ru}"


class Serie(models.Model):
    number = models.IntegerField(blank=True, null=True)
    anime_release_view_number = models.IntegerField(blank=True, null=True)
    ranobe_release_number = models.IntegerField(blank=True, null=True)
    chronological_view_number = models.IntegerField(blank=True, null=True)

    name_ru = models.CharField(max_length=100, verbose_name='Название (русский)', blank=True, null=True)
    name_en = models.CharField(max_length=100, verbose_name='Название (английский)', blank=True, null=True)
    name_jp = models.CharField(max_length=100, verbose_name='Название (японский)', blank=True, null=True)

    url = models.CharField(max_length=250, verbose_name='Ссылка', blank=True, null=True)

    description_ru = models.TextField(verbose_name='Описание (русский)', blank=True, null=True)
    description_en = models.TextField(verbose_name='Описание (английский)', blank=True, null=True)
    description_jp = models.TextField(verbose_name='Описание (японский)', blank=True, null=True)

    image_file_url =  models.TextField(verbose_name='Ссылка на изображение', blank=True, null=True)
    

    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='series')
    users = models.ManyToManyField(CustomUser, through='SerieStatus')

    def __str__(self):
        return self.name_ru


class SerieStatus(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)
    STATUS_CHOICES = (
        ('not-watched', 'Не просмотрено'),
        ('watching', 'Смотрю'),
        ('watched', 'Просмотрено'),
        ('to-watch', 'Буду смотреть'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not-watched')
    favorite = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.serie.name_ru}"


class Volume(models.Model):
    number = models.IntegerField(blank=True, null=True)
        
    name_ru = models.CharField(max_length=100, verbose_name='Название (русский)', blank=True, null=True)
    name_en = models.CharField(max_length=100, verbose_name='Название (английский)', blank=True, null=True)
    name_jp = models.CharField(max_length=100, verbose_name='Название (японский)', blank=True, null=True)

    url = models.CharField(max_length=250, verbose_name='Ссылка', blank=True, null=True)

    description_ru = models.TextField(verbose_name='Описание (русский)', blank=True, null=True)
    description_en = models.TextField(verbose_name='Описание (английский)', blank=True, null=True)
    description_jp = models.TextField(verbose_name='Описание (японский)', blank=True, null=True)

    image_file_url =  models.TextField(verbose_name='Ссылка на изображение', blank=True, null=True)
    # serie = models.ForeignKey(Serie, on_delete=models.CASCADE)
    users = models.ManyToManyField(CustomUser, through='VolumeStatus')

    def __str__(self):
        return self.name_ru


class VolumeStatus(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    volume = models.ForeignKey(Volume, on_delete=models.CASCADE)
    STATUS_CHOICES = (
        ('not-watched', 'Не просмотрено'),
        ('watching', 'Смотрю'),
        ('watched', 'Просмотрено'),
        ('to-watch', 'Буду смотреть'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not-watched')
    favorite = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.volume.name_ru}"


class Chapter(models.Model):
    number = models.IntegerField(blank=True, null=True)
    name_ru = models.CharField(max_length=100, verbose_name='Название (русский)', blank=True, null=True)
    name_en = models.CharField(max_length=100, verbose_name='Название (английский)', blank=True, null=True)
    name_jp = models.CharField(max_length=100, verbose_name='Название (японский)', blank=True, null=True)

    url = models.CharField(max_length=250, verbose_name='Ссылка', blank=True, null=True)

    description_ru = models.TextField(verbose_name='Описание (русский)', blank=True, null=True)
    description_en = models.TextField(verbose_name='Описание (английский)', blank=True, null=True)
    description_jp = models.TextField(verbose_name='Описание (японский)', blank=True, null=True)

    image_file_url =  models.TextField(verbose_name='Ссылка на изображение', blank=True, null=True)

    volume = models.ForeignKey(Volume, on_delete=models.CASCADE, related_name='chapters')
    users = models.ManyToManyField(CustomUser, through='ChapterStatus')

    def __str__(self):
        return self.name_ru


class ChapterStatus(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    STATUS_CHOICES = (
        ('not-watched', 'Не просмотрено'),
        ('watching', 'Смотрю'),
        ('watched', 'Просмотрено'),
        ('to-watch', 'Буду смотреть'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not-watched')
    favorite = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.chapter.name_ru}"