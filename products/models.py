from django.db import models

# Create your models here.
class products(models.Model):
    product_id=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=50,default='')
    weight=models.CharField(max_length=50,default='')
    price=models.IntegerField(default='')
    created_at=models.DateTimeField(auto_now_add=True,blank=True)
    updated_at=models.DateField(auto_now=True,blank=True)

    def __str__(self):
        return self.product_name