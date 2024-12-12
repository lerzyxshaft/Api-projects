from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length=100)
    anons = models.TextField()
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)  # Field name

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"

    class NewsArticle(models.Model):
        title = models.CharField(max_length=255)
        anons = models.TextField()
