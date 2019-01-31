from django.db import models

# Create your models here.
class blog(models.Model):
    title=models.CharField(max_length=100)
    body=models.TextField()
    date=models.DateTimeField()

    def __str__(self):
        return self.title

class News(models.Model):
    news=models.CharField(max_length=500)
    link=models.CharField(max_length=136,null=True,blank=True)
    def __str__(self):
        return self.news
