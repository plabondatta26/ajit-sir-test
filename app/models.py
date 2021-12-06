from django.db import models

# Create your models here.


class WriterModel(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    age = models.CharField(max_length=2, blank=False, null=False)
    bday = models.DateField(blank=False, null=False)

    def __str__(self):
        return self.name + ' ' + self.age


class BlogModel(models.Model):
    writer = models.ForeignKey(WriterModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(max_length=10000,blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.writer.name + ' ' + self.title

