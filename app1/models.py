from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    favorite_jobs = models.ManyToManyField('app1.Job', related_name='favorite_jobs')


class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    type = models.CharField(max_length=50)
    description = models.TextField()
    company_name = models.CharField(max_length=255)
    company_description = models.TextField()
    logo = models.ImageField(upload_to="logo/")
    published_on = models.DateField(auto_now_add=True, null=True, blank=True)


class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    cover_letter = models.TextField()
    cv = models.FileField(upload_to="cvs/")
