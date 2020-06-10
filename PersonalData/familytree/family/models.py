from django.db import models

# Create your models here.

class Tree(models.Model):
    familyid = models.CharField(max_length=100,unique=True)
    loginname = models.CharField(max_length=100,unique=True,default='abc')
    password = models.CharField(max_length=100,default='abc')
    familyname = models.CharField(max_length=100)
    linkingimage = models.CharField(max_length=120, default="na.jpeg", editable=True)
    email_address = models.CharField(max_length=100,default="abc@abc.com", editable=True)

    def __str__(self):
        return self.familyname

class Family(models.Model):
    SEX_CHOICES = [('M','Male'),('F','Female')]
    familyid = models.ForeignKey('Tree',on_delete=models.CASCADE,to_field='familyid')
    name = models.CharField(max_length = 100)
    fathername = models.CharField(max_length=100,default="Void")
    mothername = models.CharField(max_length=100,default="Void" )
    email_address = models.CharField(max_length = 100)
    birthplace = models.CharField(max_length = 40)
    residence = models.CharField(max_length = 100)
    spousename = models.CharField(max_length=100)
    sex = models.CharField(choices = SEX_CHOICES, max_length = 1,blank=True)
    age = models.IntegerField(null = True)
    linkimage = models.CharField(max_length=120,default = "na.jpeg",editable = True)
    otherimages = models.CharField(max_length=300,default = "na.jpeg",editable=True)
    globalid = models.CharField(max_length=100,editable=True,default='1')

    def __str__(self):
        return self.name

class Child(models.Model):
    parentid = models.ForeignKey('Family',on_delete=models.CASCADE,related_name='parentid')
    childid = models.ForeignKey('Family',on_delete=models.CASCADE,related_name='childid')

    def __str__(self):
         return self.childid.name