from django.db import models

# Create your models here.
# Database -----> Excel workbook
# Models in Django ----> Table------>Excel Sheet

class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=250)
    phone=models.CharField(max_length=15)
    email=models.CharField(max_length=100)
    content=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return "message from---"+ self.name +"---->"+self.email
    


 