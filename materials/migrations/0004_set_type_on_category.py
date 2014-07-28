# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        # Note: Don't use "from appname.models import ModelName". 
        # Use orm.ModelName to refer to models in this application,
        # and orm['appname.ModelName'] for models in other applications.
        from .. import DETAIL_TYPE
        for category in orm.Material.objects.all():
            category.type = DETAIL_TYPE
            category.save()

    def backwards(self, orm):
        "Write your backwards methods here."
        pass

    models = {
        u'core.category': {
            'Meta': {'object_name': 'Category'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Image']", 'unique': 'True', 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'})
        },
        u'core.detail': {
            'Meta': {'object_name': 'Detail'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'facts': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'subcategory': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Subcategory']"}),
            'title_image': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Image']", 'unique': 'True', 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'video_url': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'core.image': {
            'Meta': {'object_name': 'Image'},
            'alt_text': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'figcaption': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'core.subcategory': {
            'Meta': {'object_name': 'Subcategory'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Category']", 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'})
        },
        u'materials.material': {
            'Meta': {'object_name': 'Material', '_ormbases': [u'core.Category']},
            u'category_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Category']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'materials.materialdetail': {
            'Meta': {'object_name': 'MaterialDetail', '_ormbases': [u'core.Detail']},
            u'detail_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Detail']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'materials.materialsubcategory': {
            'Meta': {'object_name': 'MaterialSubcategory', '_ormbases': [u'core.Subcategory']},
            u'subcategory_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Subcategory']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['materials']
    symmetrical = True
