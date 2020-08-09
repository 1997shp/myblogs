from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class BlogType(models.Model):

    #类型
    type_name = models.CharField(max_length=15)

    def __str__(self):
        return self.type_name


class Blog(models.Model):
    #标题
    title = models.CharField(max_length=50)

    #外键 博客分类
    blog_type = models.ForeignKey(BlogType,on_delete=models.DO_NOTHING,default=1)

    #内容
    content = RichTextUploadingField()

    #作者
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING)

    #阅读数字段
    readed_num = models.IntegerField(default=0)

    #创建时间
    created_time = models.DateTimeField(auto_now_add = True)

    #最后修改时间
    last_updated_time = models.DateTimeField(auto_now = True)

    # def read_num(self):

    #     return self.ReadNum.readed_num

    def __str__(self):

        
        return "<Blog: %s>" % self.title

    class Meta:
        ordering = ["-created_time"]

class ReadNum(models.Model):

    blog = models.OneToOneField(Blog,on_delete=models.DO_NOTHING)
