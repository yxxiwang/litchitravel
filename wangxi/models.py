from django.db import models

# Create your models here.
class Member(models.Model):
    #uid = models.IntegerField()
    status = models.IntegerField(blank=True,default=0)
    regtime = models.DateTimeField('date published',blank=True)
    name = models.CharField(max_length=60,blank=True)
    password = models.CharField(max_length=200,blank=True)
    email = models.CharField(max_length=80,blank=True)
    following_count = models.IntegerField(blank=True,default=0)
    follows_count = models.IntegerField(blank=True,default=0)
    publish_count = models.IntegerField(blank=True,default=0)
    subscribe_count = models.IntegerField(blank=True,default=0)

class Message(models.Model):
    #poll = models.ForeignKey(Poll)
    #uid = models.IntegerField()
    status = models.IntegerField(default=0)
    content = models.CharField(max_length=1000,blank=True)
    publish_uid = models.ForeignKey(Member)
    publish_time = models.DateTimeField('date published')