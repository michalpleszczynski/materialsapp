# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FormSubcategory'
        db.create_table('forms_formsubcategory', (
            ('subcategory_ptr', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['core.Subcategory'], primary_key=True)),
        ))
        db.send_create_signal('forms', ['FormSubcategory'])

        # Adding model 'FormDetail'
        db.create_table('forms_formdetail', (
            ('detail_ptr', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['core.Detail'], primary_key=True)),
        ))
        db.send_create_signal('forms', ['FormDetail'])


    def backwards(self, orm):
        # Deleting model 'FormSubcategory'
        db.delete_table('forms_formsubcategory')

        # Deleting model 'FormDetail'
        db.delete_table('forms_formdetail')


    models = {
        'core.detail': {
            'Meta': {'object_name': 'Detail'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'facts': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'title_image': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['core.Image']", 'on_delete': 'models.SET_NULL', 'blank': 'True', 'null': 'True'}),
            'video_url': ('django.db.models.fields.URLField', [], {'max_length': '255'})
        },
        'core.image': {
            'Meta': {'object_name': 'Image'},
            'alt_text': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True', 'null': 'True'}),
            'figcaption': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True', 'null': 'True'})
        },
        'core.subcategory': {
            'Meta': {'object_name': 'Subcategory'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True', 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'details': ('django.db.models.fields.related.ManyToManyField', [], {'null': 'True', 'to': "orm['core.Detail']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'forms.formdetail': {
            'Meta': {'object_name': 'FormDetail', '_ormbases': ['core.Detail']},
            'detail_ptr': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['core.Detail']", 'primary_key': 'True'})
        },
        'forms.formsubcategory': {
            'Meta': {'object_name': 'FormSubcategory', '_ormbases': ['core.Subcategory']},
            'subcategory_ptr': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['core.Subcategory']", 'primary_key': 'True'})
        }
    }

    complete_apps = ['forms']