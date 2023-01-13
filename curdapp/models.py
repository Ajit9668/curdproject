from django.db import models
class empData(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.EmailField(30)
    mobile=models.BigIntegerField()
    company=models.CharField(max_length=50)
    salary=models.IntegerField()
    location=models.CharField(max_length=50)
