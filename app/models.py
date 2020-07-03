from django.db import models



# Create your models here.


class group(models.Model):
    id = models.IntegerField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)


class question(models.Model):
    id = models.IntegerField(primary_key=True)
    question = models.FileField(upload_to='files/')
    comment = models.CharField(max_length=222)
    created_at = models.DateTimeField(auto_now_add=True)
    group_id = models.ForeignKey(group, to_field='id', on_delete=models.CASCADE)
