from django.db import models
from apps.users import models as users_models
from ckeditor.fields import RichTextField
# Create your models here.

class show_pictures_index(models.Model):
    id=models.IntegerField(primary_key=True)
    description=models.TextField()
    picture=models.ImageField(upload_to='show_pictures_index')
    artical=models.ForeignKey(users_models.ArticalDetails,on_delete=models.DO_NOTHING,default=None)
    class Meta:
        verbose_name_plural='首页轮播图'
        db_table='show_pictures_index'

class Book(models.Model):
    name=models.CharField(max_length=40,verbose_name='书名')
    author=models.ForeignKey(users_models.User,on_delete=models.CASCADE)
    status=models.CharField(max_length=20,choices=(('update','连载中'),('finished','完结')))
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural='书籍'

class Book_every_colomn(models.Model):
    index_num=models.IntegerField(primary_key=True,verbose_name='章节序号')
    title=models.CharField(max_length=50,verbose_name='章节名称')
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    content=RichTextField()
    create_time=models.DateTimeField(auto_now_add=True)
    read_num=models.IntegerField(default=0)
    get_good=models.IntegerField(default=0)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural='章节详情'

class Book_colomn_details(models.Model):
    index_num=models.IntegerField(primary_key=True,verbose_name='章节序号')
    title=models.CharField(max_length=50,verbose_name='章节名称')
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    content=RichTextField()
    create_time=models.DateTimeField(auto_now_add=True)
    read_num=models.IntegerField(default=0)
    get_good=models.IntegerField(default=0)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural='章节详情'