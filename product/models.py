from django.db import models

# Create your models here.
class Customer(models.Model):
    cust_id=models.IntegerField(primary_key=True)
    cust_name=models.CharField(max_length=20)
    cust_address=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cust_name
    

class Products(models.Model):
    product_id=models.IntegerField(primary_key=True)
    product_name=models.CharField(max_length=20)
    cust_name=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product_image=models.ImageField(upload_to='items',blank=True)

    def __str__(self):
        return self.product_name
    
    
