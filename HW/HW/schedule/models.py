from django.db import models


class Exam(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    lecturer = models.CharField(max_length=50, verbose_name='Преподаватель')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Экзамен'
        verbose_name_plural = 'Экзамены'
        ordering = ['name']


class Group(models.Model):
    name = models.CharField(max_length=50, verbose_name='Номер')
    lessons = models.ManyToManyField(Exam, through='Schedule')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
        ordering = ['name']


class Schedule(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name='Группа')
    lesson = models.ForeignKey(Exam, on_delete=models.CASCADE, verbose_name='Экзамен')
    lesson_time = models.DateTimeField(default='2021-01-10', verbose_name='Время экзамена')
    consultation_time = models.DateTimeField(default='2021-01-10', verbose_name='Время консультации')

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписание'
        ordering = ['group']
