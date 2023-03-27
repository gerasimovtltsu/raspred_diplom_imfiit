from django.db import models
from smart_selects.db_fields import ChainedForeignKey


class Supervisor(models.Model):
    name = models.CharField(max_length=255, verbose_name='ФИО руководителя')
    degree = models.CharField(max_length=255, verbose_name='Ученая степень', blank=True)

    class Meta:
        verbose_name = 'Руководитель'
        verbose_name_plural = 'Руководители'
        ordering = ['name']

    def __str__(self):
        return self.name


class Topic(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название темы')
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE, verbose_name='ФИО руководителя')
    reserved_status = models.BooleanField(verbose_name='Статус резервирования')

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'
        ordering = ['title']

    def __str__(self):
        return self.title


class Record(models.Model):
    student_name = models.CharField(max_length=255, verbose_name='ФИО студента')
    supervisor_name = models.ForeignKey(Supervisor, on_delete=models.CASCADE, verbose_name='ФИО руководителя')
    topic_title = ChainedForeignKey(
        Topic,
        chained_field="supervisor_name",
        chained_model_field="supervisor",
        show_all=False,
        auto_choose=False,
        sort=True,
        limit_choices_to={'reserved_status': False}
    )

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    def __str__(self) -> str:
        return self.student_name

# модель для хранения "Архива" записей

class Archive(models.Model):
   name = models.CharField(max_length=255, verbose_name='ФИО студента')
   supervis_name = models.CharField(max_length=255, verbose_name='ФИО руководителя')
   top_title = models.CharField(max_length=255, verbose_name='Название темы')
   date_post = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Дата записи')
   
   class Meta:
        verbose_name = 'Архив'
        verbose_name_plural = 'Архивы'