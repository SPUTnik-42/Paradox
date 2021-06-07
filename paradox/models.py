from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings 

# Create your models here.
class User(AbstractUser):
    pass

class team_member(models.Model):
    level = models.IntegerField(default=0) 
    teamName = models.CharField(max_length=1000)
    alpha = models.ForeignKey(User, on_delete=models.CASCADE, related_name="alpha")
    beta = models.ForeignKey(User, on_delete=models.CASCADE, related_name="beta", null=True, blank=True)
    gamma = models.ForeignKey(User, on_delete=models.CASCADE, related_name="gamma", null=True, blank=True)

    def __str__(self):
        return self.teamName

class user_detail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="details")
    disqualified = models.BooleanField(default=False)
    user_class = models.IntegerField()
    level = models.IntegerField(default=0)  
    isschool = models.CharField(default="INTRA",max_length=300)  
    nonComp = models.IntegerField(default=0)
    isOver = models.IntegerField(default=0)
    imgURL = models.CharField(default='img', max_length=1000)
    firstuse = models.IntegerField(default=1)
    team_members = models.ForeignKey(team_member, on_delete=models.CASCADE, related_name="user_team")

    def __str__(self):
        return self.user.username  

#class team(models.Model):
    #username = models.CharField(max_length=300)
    #team = models.CharField(max_length=300)
    #time = models.DateTimeField(auto_now_add=True)



class question(models.Model):
    level = models.IntegerField(primary_key=True)
    question = models.CharField(max_length=400)
    answer = models.CharField(max_length=400)
    alt_answer = models.CharField(max_length=400)
    img = models.CharField(max_length=1000)
    no_of_hints = models.IntegerField(default=0)

    objects = models.Manager()

    def __str__(self):
        return f"qs for level {self.level}"

class log(models.Model):
    username = models.CharField(max_length=400)
    action = models.CharField(max_length=400)
    time = models.TimeField(auto_now_add=True)
    category = models.CharField(max_length=400)
    level = models.IntegerField()

    objects = models.Manager()

    def __str__(self):
        return f"{self.username} submitted {self.action}"


class hint(models.Model):
    level = models.IntegerField(primary_key=True)
    hint_text = models.CharField(max_length=400)
    time = models.TimeField(auto_now_add=True)
    hint_number = models.IntegerField()
    img = models.CharField(max_length=1000)

    objects = models.Manager()

    def __str__(self):
        return f"hint for level {self.level}"
