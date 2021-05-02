from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager,PermissionsMixin
from django.urls import reverse
from DjangoBlog.utils import get_current_site
from django.utils.timezone import now

# Create your models here.

class BlogUser(AbstractUser):
    nickname = models.CharField('昵称', max_length=100, blank=True)
    created_time = models.DateTimeField('创建时间', default=now)
    last_mod_time = models.DateTimeField('修改时间', default=now)
    source = models.CharField("创建来源", max_length=100, blank=True)

    def get_absolute_url(self):
        return reverse(
            'blog:author_detail', kwargs={
                'author_name': self.username})

    def __str__(self):
        return self.email

    def get_full_url(self):
        site = get_current_site().domain
        url = "https://{site}{path}".format(site=site,
                                            path=self.get_absolute_url())
        return url


    class Meta:
        ordering = ['-id']
        verbose_name = "用户"
        verbose_name_plural = verbose_name
        get_latest_by = 'id'





class Employe(models.Model):
    name = models.CharField(max_length=128, verbose_name='名称', help_text='员工的名字', null=False, blank=False,
                            db_index=True)

    gender_choices = (
        (0, '未知'),
        (1, '男'),
        (2, '女'),
    )

    gender = models.IntegerField(choices=gender_choices, verbose_name='性别', default=0)

    class Meta:
        verbose_name = "员工"
        verbose_name_plural = "员工管理"

        # 定义自定义的权限
        permissions = (
            ('test', 'test111'),
            ('test2', 'test222'),
            ('权限显示的名称','权限判断的code'),
            ('测试按钮','test'), # 注意 这里的test要与admin中的按钮方法名一致
            ('Simpleui','view_simpleui')
        )