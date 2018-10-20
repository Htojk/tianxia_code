from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.
class OrdernaryUser(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    nickname=models.CharField(blank=True,null=True,max_length=50)
    def __str__(self):
        return self.nickname
    class Meta:
        verbose_name='普通会员表'
        verbose_name_plural=verbose_name

class ArticalType(models.Model):
    type=models.CharField(max_length=10,choices=(('xiaoshuo','小说'),('sanwen','散文'),('shige','诗歌'),('shuping','书评')),verbose_name='文章分类')
    def __str__(self):
        return self.type
    class Meta:
        verbose_name_plural='文章分类'

class ArticalDetails(models.Model):
    title=models.CharField(max_length=50,verbose_name='标题')
    type=models.ForeignKey(ArticalType,on_delete=models.CASCADE,verbose_name='类别')
    author=models.ForeignKey(OrdernaryUser,on_delete=models.CASCADE,verbose_name='作者')
    read_num=models.IntegerField(default=0,verbose_name='浏览量')
    create_time=models.DateTimeField(auto_now_add=True)
    content=RichTextField()
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural='文章'
