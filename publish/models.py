from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    _title = models.CharField("Название", max_length = 48)
    _content = models.TextField('Кантент', max_length = 4000)
    _pub_date = models.DateField('Дата публикации')

    def __str__(self):
        return  self._title

class Comment(models.Model):
    _origin = models.ForeignKey(Article, on_delete = models.CASCADE)
    _author = models.CharField('Автор', max_length = 36) 
    _content = models.TextField('Коментарий', max_length = 400)

    def __str__(self):
        return self._author

    @staticmethod
    def time():
        print('hellp')