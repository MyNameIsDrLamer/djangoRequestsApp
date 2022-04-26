import os
from django.db import models
from simple_history.models import HistoricalRecords


class Request(models.Model):
    Customers_full_name = models.CharField(max_length=50, verbose_name='Заказчик', blank=False)
    Lecture_hall = models.CharField(max_length=10, verbose_name='Аудитория', blank=False)
    Description = models.TextField(max_length=150, blank=True, verbose_name='Описание')
    Work = models.ForeignKey('Type_of_work_list', on_delete=models.DO_NOTHING, verbose_name='Тип работ', blank=False)
    Performer = models.ForeignKey('Full_name_of_the_performer_list', on_delete=models.DO_NOTHING,
                                  verbose_name='Исполнитель', blank=False)
    Comment = models.TextField(max_length=150, blank=True, verbose_name='Комментарий исполнителя')
    Files = models.FileField(upload_to='./static' + '/files' + '/%Y/%m/%d/', verbose_name='Загрузка файла', blank=True)
    Request_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата заявки')
    Condition = models.ForeignKey('Condition_list', on_delete=models.DO_NOTHING, verbose_name='Состояние', blank=False)
    History = HistoricalRecords()

    def __str__(self):
        return f"{self.Customers_full_name}"

    def get_absolute_url(self):
        return '/'

    class Meta:
        ordering = ['-pk']
        verbose_name = 'Заявки'
        verbose_name_plural = 'Заявки'


class Type_of_work_list(models.Model):
    Type_of_work = models.CharField(max_length=50, db_index=True, unique=True, verbose_name='Вид работ')
    History = HistoricalRecords()

    def __str__(self):
        return f"{self.Type_of_work}"

    class Meta:
        verbose_name = 'Виды работ'
        verbose_name_plural = 'Виды работ'
        ordering = ['Type_of_work']


class Condition_list(models.Model):
    Condition = models.CharField(max_length=15, db_index=True, verbose_name='Состояние')
    History = HistoricalRecords()

    def __str__(self):
        return self.Condition

    class Meta:
        verbose_name = 'Состояния'
        verbose_name_plural = 'Состояния'
        ordering = ['Condition']


class Full_name_of_the_performer_list(models.Model):
    Full_name_of_the_performer = models.CharField(max_length=50, db_index=True, unique=True, verbose_name='Ф.И.О. '
                                                                                                          'исполнителя')
    History = HistoricalRecords()

    def __str__(self):
        return f"{self.Full_name_of_the_performer}"

    class Meta:
        verbose_name = 'Исполнители'
        verbose_name_plural = 'Исполнители'
        ordering = ['Full_name_of_the_performer']