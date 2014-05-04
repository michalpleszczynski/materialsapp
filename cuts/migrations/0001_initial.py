# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CutSubcategory'
        db.create_table('cuts_cutsubcategory', (
            ('subcategory_ptr', self.gf('django.db.models.fields.related.OneToOneField')(primary_key=True, to=orm['core.Subcategory'], unique=True)),
        ))
        db.send_create_signal('cuts', ['CutSubcategory'])

        # Adding model 'CutDetail'
        db.create_table('cuts_cutdetail', (
            ('detail_ptr', self.gf('django.db.models.fields.related.OneToOneField')(primary_key=True, to=orm['core.Detail'], unique=True)),
        ))
        db.send_create_signal('cuts', ['CutDetail'])


    def backwards(self, orm):
        # Deleting model 'CutSubcategory'
        db.delete_table('cuts_cutsubcategory')

        # Deleting model 'CutDetail'
        db.delete_table('cuts_cutdetail')


    models = {
        'core.detail': {
            'Meta': {'object_name': 'Detail'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'}),
            'facts': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'title_image': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Image']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True', 'unique': 'True'}),
            'video_url': ('django.db.models.fields.URLField', [], {'max_length': '255'})
        },
        'core.image': {
            'Meta': {'object_name': 'Image'},
            'alt_text': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '50', 'blank': 'True'}),
            'figcaption': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '150', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.URLField', [], {'null': 'True', 'max_length': '255', 'blank': 'True'})
        },
        'core.subcategory': {
            'Meta': {'object_name': 'Subcategory'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'caption': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '500', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'}),
            'details': ('django.db.models.fields.related.ManyToManyField', [], {'null': 'True', 'to': "orm['core.Detail']", 'blank': 'True', 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'cuts.cutdetail': {
            'Meta': {'object_name': 'CutDetail', '_ormbases': ['core.Detail']},
            'detail_ptr': ('django.db.models.fields.related.OneToOneField', [], {'primary_key': 'True', 'to': "orm['core.Detail']", 'unique': 'True'})
        },
        'cuts.cutsubcategory': {
            'Meta': {'object_name': 'CutSubcategory', '_ormbases': ['core.Subcategory']},
            'subcategory_ptr': ('django.db.models.fields.related.OneToOneField', [], {'primary_key': 'True', 'to': "orm['core.Subcategory']", 'unique': 'True'})
        }
    }

    complete_apps = ['cuts']