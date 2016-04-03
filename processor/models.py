from django.db import models

class Creator(models.Model):
    name = models.CharField(primary_key=True, max_length=200)
    profileUrl = models.SlugField(max_length=200)
    
    def __str__(self):
        return self.name

class Prezi(models.Model):
    id = models.CharField(primary_key=True, max_length=200)
    title = models.CharField(max_length=200)
    thumbnail = models.SlugField(max_length=200)
    creator = models.ForeignKey(Creator)
    pub_date = models.DateTimeField()
    
    def __str__(self):
        return self.id
