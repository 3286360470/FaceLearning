from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
#用户表：编号，名称，邮箱，创建时间，更新时间
# class User(models.Model):
#     uid = models.AutoField(primary_key=True)
#     uname = models.CharField(max_length=30)
#     email = models.EmailField()
#     create_time = models.DateField()
#     update_time = models.DateField()
#
#     def __str__(self):
#         return self.uid

class User(AbstractUser):
    nickname = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return str(self.username)
    class Meta(AbstractUser.Meta):
        pass

#原始图片：编号，图片内容，名称，状态，创建时间，更新时间
class OriPic(models.Model):
    opid = models.AutoField(primary_key=True)
    # image = models.CharField(max_length=500)
    imageOri = models.ImageField(upload_to='imgOri')
    opname = models.CharField(max_length=50)
    opstate = models.IntegerField()
    create_time = models.DateField()
    update_time = models.DateField()

    def __str__(self):
        return str(self.imageOri)

#目标图片：编号，图片内容，名称，状态，创建时间，更新时间
class TarPic(models.Model):
    tpid = models.AutoField(primary_key=True)
    imageTar = models.ImageField(upload_to='imgTar')
    tpname = models.CharField(max_length=50)
    tpstate = models.IntegerField()
    create_time = models.DateField()
    update_time = models.DateField()

    def __str__(self):
        return str(self.imageTar)

#历史记录列表：编号，记录中的任务数，关联的用户，关联的原始图片和目标图片，创建时间，更新时间
class Record(models.Model):
    rid = models.AutoField(primary_key=True)
    amount = models.IntegerField()
    users = models.ForeignKey(User, on_delete=models.CASCADE,)
    oripics = models.ManyToManyField(OriPic)
    tarpics = models.ManyToManyField(TarPic)
    create_time = models.DateField()
    update_time = models.DateField()

    def __str__(self):
        return self.rid


#test
class Test(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField(max_length=200)

    def __str__(self):
        return self.id

