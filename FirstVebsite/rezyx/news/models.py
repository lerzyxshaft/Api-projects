from django.db import models

class Articles(models.Model):
    title = models.CharField('Name',max_length=50)
    anons = models.TextField('Anons', max_length=250)
    full_text = models.TextField('Post')
    date = models.DateTimeField('Publish date')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
