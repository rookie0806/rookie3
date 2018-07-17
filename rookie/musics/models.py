from django.db import models

# Create your models here.

class Music(models.Model):
    Music_name = models.CharField(max_length=100,default="")
    Singer_name = models.CharField(max_length=100,default="")
    Grade = models.IntegerField(default=0) # 순위
    Melon_serial = models.IntegerField(default=0)
    Naver_serial = models.IntegerField(default=0)
    Bugs_serial = models.IntegerField(default=0)
    Genie_serial = models.IntegerField(default=0)
    Serial_nubmer = models.AutoField(primary_key=True)
    def __str__(self):
        return '{}-{}'.format(self.Music_name, self.Singer_name)