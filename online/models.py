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
    def __unicode__(self):
        return self.username
# Create your models here.
