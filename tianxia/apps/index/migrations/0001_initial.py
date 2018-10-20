# Generated by Django 2.1.1 on 2018-10-11 00:16

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='书名')),
                ('status', models.CharField(choices=[('update', '连载中'), ('finished', '完结')], max_length=20)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '书籍',
            },
        ),
        migrations.CreateModel(
            name='Book_every_colomn',
            fields=[
                ('index_num', models.IntegerField(primary_key=True, serialize=False, verbose_name='章节序号')),
                ('title', models.CharField(max_length=50, verbose_name='章节名称')),
                ('content', ckeditor.fields.RichTextField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('read_num', models.IntegerField(default=0)),
                ('get_good', models.IntegerField(default=0)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Book')),
            ],
            options={
                'verbose_name_plural': '章节详情',
            },
        ),
        migrations.CreateModel(
            name='show_pictures_index',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('picture', models.ImageField(upload_to='show_pictures_index')),
                ('artical', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='users.ArticalDetails')),
            ],
            options={
                'verbose_name_plural': '首页轮播图',
                'db_table': 'show_pictures_index',
            },
        ),
    ]
