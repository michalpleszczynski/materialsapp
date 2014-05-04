# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Detail.video_url'
        db.alter_column('core_detail', 'video_url', self.gf('django.db.models.fields.URLField')(max_length=255, null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Detail.video_url'
        raise RuntimeError("Cannot reverse this migration. 'Detail.video_url' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Detail.video_url'
        db.alter_column('core_detail', 'video_url', self.gf('django.db.models.fields.URLField')(max_length=255))

    models = {
        'core.category': {
            'Meta': {'object_name': 'Category'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Image']", 'on_delete': 'models.SET_NULL', 'unique': 'True', 'blank': 'True', 'null': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'subcategories': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['core.Subcategory']", 'related_name': "'categories'", 'symmetrical': 'False', 'blank': 'True', 'null': 'True'})
        },
        'core.detail': {
            'Meta': {'object_name': 'Detail'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'}),
            'facts': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'title_image': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Image']", 'on_delete': 'models.SET_NULL', 'unique': 'True', 'blank': 'True', 'null': 'True'}),
            'video_url': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '255', 'null': 'True'})
        },
        'core.detailsection': {
            'Meta': {'object_name': 'DetailSection'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'}),
            'detail': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Detail']", 'related_name': "'sections'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30', 'null': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'})
        },
        'core.detailsectionimage': {
            'Meta': {'object_name': 'DetailSectionImage', '_ormbases': ['core.Image']},
            'image_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Image']", 'unique': 'True', 'primary_key': 'True'}),
            'subcategory': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.DetailSection']", 'related_name': "'images'"})
        },
        'core.image': {
            'Meta': {'object_name': 'Image'},
            'alt_text': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '50', 'null': 'True'}),
            'figcaption': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '150', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '255', 'null': 'True'})
        },
        'core.subcategory': {
            'Meta': {'object_name': 'Subcategory'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'caption': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '500', 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'}),
            'details': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['core.Detail']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        }
    }

    complete_apps = ['core']