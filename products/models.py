from django.db import models

# models fir products
class Product(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'live'),(DELETE,'Delete'))
    title=models.CharField(max_length=200)
    price=models.FloatField()
    description=models.TextField()
    image=models.ImageField(upload_to='media/')
    priority=models.IntegerField(default=0)
    create_at=models.DateTimeField(auto_now_add=True)
    upated_at=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title