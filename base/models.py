from django.db import models

class upload_product(models.Model):
    product_id=models.AutoField(primary_key=True)
    product_t=models.TextField(max_length=200)
    product_n=models.TextField(max_length=100)
    product_p=models.IntegerField()
    product_d=models.IntegerField()
    product_i=models.ImageField(upload_to='products')
    product_c=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_n
    


 

