from django.db import models#do not understand only key
class User(models.Model):
    name = models.CharField(max_length=50)
    passwd = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    beans = models.IntegerField()
    vip = models.BinaryField()
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    role = models.CharField(max_length=255, blank=True)
    head_image = models.ImageField(upload_to='images',max_length=255,blank=True, null=True)
    comp = models.CharField(max_length=50)
    job = models.CharField(max_length=50)
    edu = models.CharField(max_length=50)
    
    
    mycomp = models.CharField(max_length=50)
    myjob = models.CharField(max_length=50)
    mymoney = models.CharField(max_length=50)
    myintr = models.CharField(max_length=254)
    mylocal = models.CharField(max_length=50)
    mymoney = models.CharField(max_length=255)
# Create your models here.
