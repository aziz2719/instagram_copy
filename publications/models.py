from django.db import models
from django.conf import settings

class Publications(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, 'post_owner')
    text = models.TextField('Текст')
    date = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
        #ordering = ('-date', )

    def __str__(self):
        return self.text

class PublicationImages(models.Model):
    publication = models.ForeignKey('publications.Publications', models.CASCADE, 'post_images')
    image = models.FileField('Фото', upload_to = 'post_images')

class Comments(models.Model):
    text = models.TextField()
    publication = models.ForeignKey('publications.Publications', models.CASCADE, 'post_comments')
    owner = models.ForeignKey('user.User', models.CASCADE, 'user_comments')
    created_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.text

class Likes(models.Model):
    publication = models.ForeignKey('publications.Publications', models.CASCADE, 'post_likes')
    user = models.ForeignKey('user.User', models.SET_NULL, 'likes_from_user', null=True)