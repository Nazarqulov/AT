from django.db import models
class Muallim(models.Model):
    ismi=models.CharField(max_length=200)
    familiyasi=models.CharField(max_length=200)
    yoshi=models.IntegerField(default=1)
    ilmiy_salohiyati=models.CharField(max_length=200)
    mutaxassisligi=models.CharField(max_length=200)
    def __str__(self):
        return self.ismi
    class Meta:
        db_table = 'Muallim'
        verbose_name = 'Muallim'
class News(models.Model):
    nomi=models.CharField(max_length=200,verbose_name="yangliklar")
    rasmi=models.ImageField(upload_to="images/")
    izoh=models.TextField(max_length=2000,verbose_name="izoh")
    def __str__(self):
        return self.nomi
    class Meta:
        db_table = 'News'
        verbose_name = 'News'

# Create your models here.
