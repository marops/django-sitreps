from django.db import models
import datetime
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Sitreps(models.Model):
    title = models.CharField(max_length=200,default='SITREP '+datetime.datetime.now().strftime("%Y-%m-%d"))
    pub_date = models.DateTimeField('pub date',null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(null=True, blank=True)
    #text = models.TextField('text', null=True, blank=True)
    text = RichTextUploadingField('text', null=True, blank=True)

    def save(self, *args, **kwargs):
        self.modified=datetime.datetime.now()
        super().save(*args, **kwargs)  # Call the "real" save() method.

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "SITREPS"