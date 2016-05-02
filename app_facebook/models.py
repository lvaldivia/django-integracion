from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    
    class Meta:
        db_table = "app_facebook_users"
        
    fb_id = models.BigIntegerField(null=False,db_index=True,
        verbose_name=u'FB_ID')
    first_name = models.CharField(null=False,max_length=200,
        verbose_name=u'Nombres')
    last_name = models.CharField(null=False,max_length=200,
        verbose_name=u'Apellidos')
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=u'Fecha de creacion'
    )
    updated_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=u'Fecha de actualizacion'
    )
    
    
class UserScores(models.Model):
    
    class Meta:
        db_table = "app_facebook_user_score"
        
    user = models.ForeignKey(User,null=False)
        
    score = models.IntegerField(null=False,
            verbose_name=u'puntaje')
    created_at = models.DateTimeField(
        auto_now_add = True,
        verbose_name=u'Fecha creacion'
    )
    
    
class Settings(models.Model):
    
    class Meta:
        db_table = "app_facebook_settings"
        
    app_id = models.CharField(null=False,max_length=200,
        verbose_name=u'App ID')
        
    def __unicode__(self):
        return self.app_id