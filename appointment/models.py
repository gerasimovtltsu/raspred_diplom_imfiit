from django.db import models

class Supervisor(models.Model):
    name = models.CharField(max_length=255, verbose_name='ФИО руководителя')
    degree = models.CharField(max_length=255, verbose_name='Ученая степень')

    def __str__(self):
        return self.name


class Topic(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название темы')
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE, verbose_name='Руководитель')
    reserved_status = models.BooleanField(verbose_name='Статус резервирования')

    def __str__(self):
        return self.title

class Record(models.Model):
    student_name = models.CharField(max_length=255, verbose_name='ФИО студента')
    topic_title = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name='Наименование темы')
    supervisor_name = models.ForeignKey(Supervisor, on_delete=models.CASCADE, verbose_name='ФИО руководителя')
