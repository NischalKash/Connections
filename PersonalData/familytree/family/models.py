from django.db import models

# Create your models here.

class Family(models.Model):
    SEX_CHOICES = [('M','Male'),('F','Female')]
    name = models.CharField(max_length = 100)
    email_address = models.CharField(max_length = 100)
    birthplace = models.CharField(max_length = 40)
    residence = models.CharField(max_length = 100)
    spousename = models.CharField(max_length=100)
    sex = models.CharField(choices = SEX_CHOICES, max_length = 1,blank=True)
    age = models.IntegerField(null = True)
    linkimage = models.CharField(max_length=120,default = "na.jpeg",editable = True)
    otherimages = models.CharField(max_length=300,default = "na.jpeg",editable=True)

    def __str__(self):
        return self.name

class Child(models.Model):
    parentid = models.ForeignKey('Family',on_delete=models.CASCADE,related_name='parentid')
    childid = models.ForeignKey('Family',on_delete=models.CASCADE,related_name='childid')

    def __str__(self):
         return self.childid.name