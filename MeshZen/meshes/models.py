from django.db import models

class ZenodoDeposition(models.Model):
    title = models.CharField(max_length=255)
    deposition_id = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    keywords = models.TextField(blank=True)
    created_date = models.DateTimeField()
    published_date = models.DateTimeField()
    spine_mesh_files = models.ManyToManyField('MeshFile')

class MeshFile(models.Model):
    filename = models.CharField(max_length=255)
    size = models.IntegerField()
    download_url = models.URLField()
    deposition = models.ForeignKey(ZenodoDeposition, on_delete=models.CASCADE)
