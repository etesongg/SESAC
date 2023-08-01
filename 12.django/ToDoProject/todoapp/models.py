from django.db import models

# Create your models here.
class ToDo(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True, null=True) # 해당 레코드 생성시 현재 시간 자동저장
    updated_at = models.DateTimeField(auto_now=True, null=True) # 해당 레코드 갱신시 현재 시간 자동저장