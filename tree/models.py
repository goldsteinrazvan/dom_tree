from django.db import models

# Create your models here.
class Element(models.Model):
    tag = models.CharField(max_length=50)
    _id = models.CharField(max_length=200, blank=True, null=True)
    _class = models.TextField(blank=True, null=True)
    style = models.TextField(blank=True, null=True)
    attributes = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    lft = models.IntegerField()
    rgt = models.IntegerField()

    def __str__(self):
        return '%s %s %s %s %s' % (self.tag, self._id, self.content, self.lft, self.rgt)

