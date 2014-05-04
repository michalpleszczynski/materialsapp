# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FinishSubcategory'
        db.create_table('finishes_finishsubcategory', (
            ('subcategory_ptr', self.gf('django.db.models.fields.related.OneToOneField')(primary_key=True, unique=True, to=orm['core.Subcategory'])),
        ))
        db.send_create_signal('finishes', ['FinishSubcategory'])

        # Adding model 'FinishDetail'
        db.create_table('finishes_finishdetail', (
            ('detail_ptr', self.gf('django.db.models.fields.related.OneToOneField')(primary_key=True, unique=True, to=orm['core.Detail'])),
        ))
        db.send_create_signal('finishes', ['FinishDetail'])


    def backwards(self, orm):
        # Deleting model 'FinishSubcategory'
        db.delete_table('finishes_finishsubcategory')

        # Deleting model 'FinishDetail'
        db.delete_table('finishes_finishdetail')


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
            'title_image': ('django.db.models.fields.related.OneToOneField', [], {'null': 'True', 'unique': 'True', 'to': "orm['core.Image']", 'blank': 'True', 'on_delete': 'models.SET_NULL'}),
            'video_url': ('django.db.models.fields.URLField', [], {'max_length': '255'})
        },
        'core.image': {
            'Meta': {'object_name': 'Image'},
            'alt_text': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'figcaption': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'core.subcategory': {
            'Meta': {'object_name': 'Subcategory'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'details': ('django.db.models.fields.related.ManyToManyField', [], {'null': 'True', 'symmetrical': 'False', 'to': "orm['core.Detail']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'finishes.finishdetail': {
            'Meta': {'_ormbases': ['core.Detail'], 'object_name': 'FinishDetail'},
            'detail_ptr': ('django.db.models.fields.related.OneToOneField', [], {'primary_key': 'True', 'unique': 'True', 'to': "orm['core.Detail']"})
        },
        'finishes.finishsubcategory': {
            'Meta': {'_ormbases': ['core.Subcategory'], 'object_name': 'FinishSubcategory'},
            'subcategory_ptr': ('django.db.models.fields.related.OneToOneField', [], {'primary_key': 'True', 'unique': 'True', 'to': "orm['core.Subcategory']"})
        }
    }

    complete_apps = ['finishes']