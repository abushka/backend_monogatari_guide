from django.db import models
from auth_user.models import CustomUser
from django_resized import ResizedImageField

# Seasons

class Season(models.Model):
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

    image = ResizedImageField(default='', size=[512, 512], quality=100, upload_to='season_pictures/', blank=True)

    users = models.ManyToManyField(CustomUser, through='SeasonStatus')

    def __str__(self):
        return self.name_ru
    
    def image_url(self, request):
        if self.image != '':
            return request.scheme + '://' + request.get_host() + str(self.image.url)
        else:
            return None


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
    

class SeasonImage(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='images')
    image = ResizedImageField(size=[512, 512], quality=100, upload_to='season_pictures/')

    def image_url(self, request):
        if self.image != '':
            return request.scheme + '://' + request.get_host() + str(self.image.url)
        else:
            return None


# Series

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

    image = ResizedImageField(default='', size=[512, 512], quality=100, upload_to='serie_pictures/', blank=True)
    

    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='series')
    users = models.ManyToManyField(CustomUser, through='SerieStatus')

    def __str__(self):
        return self.name_ru
    
    def image_url(self, request):
        if self.image != '':
            return request.scheme + '://' + request.get_host() + str(self.image.url)
        else:
            return None


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
    

class SerieImage(models.Model):
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE, related_name='images')
    image = ResizedImageField(size=[512, 512], quality=100, upload_to='serie_pictures/')

    def image_url(self, request):
        if self.image != '':
            return request.scheme + '://' + request.get_host() + str(self.image.url)
        else:
            return None


# Volumes

class Volume(models.Model):
    number = models.IntegerField(blank=True, null=True)
        
    name_ru = models.CharField(max_length=100, verbose_name='Название (русский)', blank=True, null=True)
    name_en = models.CharField(max_length=100, verbose_name='Название (английский)', blank=True, null=True)
    name_jp = models.CharField(max_length=100, verbose_name='Название (японский)', blank=True, null=True)

    url = models.CharField(max_length=250, verbose_name='Ссылка', blank=True, null=True)

    description_ru = models.TextField(verbose_name='Описание (русский)', blank=True, null=True)
    description_en = models.TextField(verbose_name='Описание (английский)', blank=True, null=True)
    description_jp = models.TextField(verbose_name='Описание (японский)', blank=True, null=True)

    image = ResizedImageField(default='', size=[512, 512], quality=100, upload_to='volume_pictures/', blank=True)
    # serie = models.ForeignKey(Serie, on_delete=models.CASCADE)
    users = models.ManyToManyField(CustomUser, through='VolumeStatus')

    def __str__(self):
        return self.name_ru
    
    def image_url(self, request):
        if self.image != '':
            return request.scheme + '://' + request.get_host() + str(self.image.url)
        else:
            return None


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
    

class VolumeImage(models.Model):
    volume = models.ForeignKey(Volume, on_delete=models.CASCADE, related_name='images')
    image = ResizedImageField(size=[512, 512], quality=100, upload_to='volume_pictures/')

    def image_url(self, request):
        if self.image != '':
            return request.scheme + '://' + request.get_host() + str(self.image.url)
        else:
            return None


# Chapters

class Chapter(models.Model):
    number = models.IntegerField(blank=True, null=True)
    name_ru = models.CharField(max_length=100, verbose_name='Название (русский)', blank=True, null=True)
    name_en = models.CharField(max_length=100, verbose_name='Название (английский)', blank=True, null=True)
    name_jp = models.CharField(max_length=100, verbose_name='Название (японский)', blank=True, null=True)

    url = models.CharField(max_length=250, verbose_name='Ссылка', blank=True, null=True)

    description_ru = models.TextField(verbose_name='Описание (русский)', blank=True, null=True)
    description_en = models.TextField(verbose_name='Описание (английский)', blank=True, null=True)
    description_jp = models.TextField(verbose_name='Описание (японский)', blank=True, null=True)

    image = ResizedImageField(default='', size=[512, 512], quality=100, upload_to='chapter_pictures/', blank=True)

    volume = models.ForeignKey(Volume, on_delete=models.CASCADE, related_name='chapters')
    users = models.ManyToManyField(CustomUser, through='ChapterStatus')

    def __str__(self):
        return self.name_ru
    
    def image_url(self, request):
        if self.image != '':
            return request.scheme + '://' + request.get_host() + str(self.image.url)
        else:
            return None


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
    

class ChapterImage(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='images')
    image = ResizedImageField(size=[512, 512], quality=100, upload_to='chapter_pictures/')

    def image_url(self, request):
        if self.image != '':
            return request.scheme + '://' + request.get_host() + str(self.image.url)
        else:
            return None