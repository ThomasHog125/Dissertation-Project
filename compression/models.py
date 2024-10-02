from django.db import models



#data model for the file that will be input by user 
class fileInput(models.Model):
    file = models.FileField(upload_to='compression/algorithms')
