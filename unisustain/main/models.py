from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import admin

looking = (
    ('Looking to Join', 'Looking to Join'),
    ('Looking for Researchers', 'Looking for Researchers'),
)

class Post(models.Model):
    postID = models.AutoField(primary_key = True, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.TextField()
    content = models.TextField()
    search = models.TextField(choices = looking)
    tags = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        managed = True
        db_table = 'Post'

class Question(models.Model):
    questionID = models.AutoField(primary_key = True, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.TextField()
    content = models.TextField(default = "")
    tags = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        managed = True
        db_table = 'Question'

class Postcomment(models.Model):
    postcommentID = models.AutoField(primary_key = True, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    comment = models.TextField()

    def __str__(self):
        return self.comment

    class Meta:
        managed = True
        db_table = 'Postcomment'

class Questioncomment(models.Model):
    questioncommentID = models.AutoField(primary_key = True, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    comment = models.TextField()

    def __str__(self):
        return self.comment

    class Meta:
        managed = True
        db_table = 'Questioncomment'

class Fund(models.Model):
    fundID = models.AutoField(primary_key = True, null=False)
    fundname = models.CharField(max_length = 255)
    tags = models.TextField()
    sponsor = models.CharField(max_length = 255, default = "")
    school = models.CharField(max_length = 255, default = "")
    description = models.TextField(default = "")
    info = models.TextField(default = "")
    applink = models.TextField(default = "")

    def __str__(self):
        return self.fundname

    class Meta:
        managed = True
        db_table = 'Fund'

class Event(models.Model):
    eventID = models.AutoField(primary_key = True, null=False)
    eventname = models.CharField(max_length = 255)
    eventdate = models.DateTimeField(null=True)
    tags = models.TextField()
    school = models.CharField(max_length = 255, default = "")
    description = models.TextField(default = "")
    info = models.TextField(default = "")
    applink = models.TextField(default = "")

    def __str__(self):
        return self.eventname

    class Meta:
        managed = True
        db_table = 'Event'


admin.site.register(Post)
admin.site.register(Question)
admin.site.register(Postcomment)
admin.site.register(Questioncomment)
admin.site.register(Fund)
admin.site.register(Event)
