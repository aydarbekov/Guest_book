from django.db import models

NOTE_CATEGORY_CHOICES = (
    ('active', 'Активно'),
    ('blocked', 'Заблокировано'),
)

class Note(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя автора')
    mail = models.EmailField(verbose_name='Почта автора')
    text = models.TextField(max_length=2000, verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время создания')
    status = models.CharField(max_length=20, verbose_name='Статус',
                                choices=NOTE_CATEGORY_CHOICES, default=NOTE_CATEGORY_CHOICES[0][0])

    def __str__(self):
        return self.name
