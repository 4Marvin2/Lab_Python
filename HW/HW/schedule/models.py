from django.db import models


class Exam(models.Model):
    name = models.CharField(max_length=50)
    lecturer = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=50)
    lessons = models.ManyToManyField(Exam, through='Schedule')

    def __str__(self):
        return self.name


class Schedule(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Exam, on_delete=models.CASCADE)
    lesson_time = models.DateTimeField()
