from django.db import models


class ModelWithBasicField(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        app_label = 'testapp'

    def __unicode__(self):
        return u'%s' % self.pk



class ModelWithParentModel(ModelWithBasicField):
    foo = models.BooleanField(default=False)

    class Meta:
        app_label = 'testapp'
