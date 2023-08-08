from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(null=True,blank=True,max_length=200)

class Message(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE,related_name='chat_user')
    reciever = models.ForeignKey(User,on_delete=models.CASCADE,related_name='reciever_chat',null=True,blank=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "chat_message"
        ordering = ('timestamp',)