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
    user = models.CharField(max_length=100)

    def __str__(self):
        print(self.text)


class Media(models.Model):

    tweet_id = models.CharField(max_length=250, null=True, blank=True)
    media_url = models.CharField(max_length=100, null=True, blank=True)
    media_type = models.CharField(max_length=20)




