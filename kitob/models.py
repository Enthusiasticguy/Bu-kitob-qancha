from django.db import models

# Create your models here.
class Kitob(models.Model):
    nomi = models.CharField(max_length=300)
    tarif = models.TextField(null=True, blank=True)
    slug = models.SlugField(max_length = 250, unique=True, null = True, blank = True)
    image = models.ImageField(upload_to='images', blank=True)
    narx_sana = models.DateField()
    muallif = models.CharField(max_length=300) 
    olchami = models.CharField(max_length=50)
    nashriyot = models.CharField(max_length=300)
    sana = models.DateField()
    hajm = models.PositiveIntegerField()
    muqova = models.CharField(max_length=50)
    dokonlar = models.TextField(null=True)
    class Meta:
      verbose_name_plural = "Kitoblar"
    def __str__(self):
        return self.nomi
    
