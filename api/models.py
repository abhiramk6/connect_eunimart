from django.db import models


# Create your models here.


class user(models.Model):
    genders = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('OT', 'Others'),
    )
    idd = models.AutoField(primary_key=True)
    First_name = models.CharField(max_length=32)
    Middle_name = models.CharField(max_length=32)
    Last_name = models.CharField(max_length=32)
    user_id = models.CharField(max_length=32)
    Gender = models.CharField(max_length=32, choices=genders)
    Age = models.IntegerField()
    Phone = models.CharField(max_length=10)
    Email = models.EmailField()
    Password = models.CharField(max_length=100)

    def __str__(self):
        return self.user_id


class tweet(models.Model):

    created_date = models.DateTimeField(auto_now=True)
    tweet = models.TextField()
    userid = models.ForeignKey(user, on_delete=models.CASCADE)




