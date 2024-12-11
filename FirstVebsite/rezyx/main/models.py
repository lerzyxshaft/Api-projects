from django.db import models

class Articles(models.Model):
    title = models.CharField('Name', max_length=50, default='name')
    announcements = models.CharField('announcement', max_length=250, default='name')
    full_text = models.TextField('Article')
    date = models.DateTimeField('Publication date')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"
