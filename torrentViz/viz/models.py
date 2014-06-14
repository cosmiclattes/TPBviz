from django.db import models

# Create your models here.
class TPBTopList(models.Model):
    name = models.CharField(max_length=500)
    author = models.CharField(max_length=100)
    hasCover = models.BooleanField(default = False)
    leechers = models.IntegerField(null = True)
    seeders = models.IntegerField(null = True)
    trackerUrl1 = models.TextField(null= True)
    trackerUrl2 = models.TextField(null = True)
    trackerUrl3 = models.TextField(null = True)
    trackerOthers = models.TextField(null = True)
    uploadedDate = models.DateField(null = True)
    uploadedTime = models.CharField(max_length=20, null = True)
    torrentUrl = models.TextField()
    infoHash = models.CharField(max_length=40,primary_key=True)
    attrTpbStatus = models.CharField(max_length=20,null = True)
    attrNoOfComments = models.PositiveSmallIntegerField(null=True)
    attrCats = models.TextField(null = True)
    size = models.IntegerField(null = True)
    
    def getSize(self):
        pass