from django.db import models

# Create your models here.


class Student(models.Model):
    STATUS = (
        ('неуд', 'неудовлетворительно'),
        ('уд', 'удовлетворительно'),
        ('хор', 'хорошо'),
        ('отл', 'отлично'),
    )
    name = models.CharField('ФИО', max_length=200, db_index=True)
    birthday = models.DateField('Дата рождения')
    progress = models.CharField(max_length=4, choices=STATUS, help_text='Успеваемость')

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f'ФИО: {self.name}, дата рождения: {self.birthday}, успеваемость: {self.progress}'
