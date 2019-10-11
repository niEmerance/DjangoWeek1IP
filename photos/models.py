from django.db import models
# Create your models here.

class ImageLocation(models.Model):
    locName=models.CharField(max_length =30)

    def __str__(self):
        return self.locName

class ImageCategory(models.Model):
    imgCategory=models.CharField(max_length =30)

    def __str__(self):
        return self.imgCategory
class Image(models.Model):
    imgName=models.CharField(max_length =30)
    imgDesc=models.TextField()
    imgLoc=models.ForeignKey(ImageLocation)
    imgCtgry=models.ForeignKey(ImageCategory)

    def __str__(self):
        return self.imgName

    def save_editor(self):
        self.save()
