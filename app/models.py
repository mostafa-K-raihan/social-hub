from django.db import models

# Create your models here.


class Access(models.Model):

    date = models.DateTimeField()
    return_count = models.IntegerField()
    user = models.IntegerField()


class Tweet(models.Model):

    uuid = models.CharField(max_length=250, null=True, blank=True)
    text = models.TextField()
    date = models.DateTimeField(blank=True, null=True)
    insert_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        print(self.text)




