from django.db import models

# Create your models here.
class list(models.Model):
    listTitle=models.CharField(max_length=30)
    listDes= models.TextField()
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.listTitle