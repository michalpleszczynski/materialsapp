# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Material'
        db.create_table('materials_material', (
            ('category_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Category'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('materials', ['Material'])

        # Adding model 'MaterialSubcategory'
        db.create_table('materials_materialsubcategory', (
            ('subcategory_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Subcategory'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('materials', ['MaterialSubcategory'])

        # Adding model 'MaterialDetail'
        db.create_table('materials_materialdetail', (
            ('detail_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Detail'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('materials', ['MaterialDetail'])


    def backwards(self, orm):
        # Deleting model 'Material'
        db.delete_table('materials_material')

        # Deleting model 'MaterialSubcategory'
        db.delete_table('materials_materialsubcategory')

        # Deleting model 'MaterialDetail'
        db.delete_table('materials_materialdetail')


    models = {
        'core.category': {
            'Meta': {'object_name': 'Category'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Image']", 'unique': 'True', 'null': 'True', 'blank': 'True', 'on_delete': 'models.SET_NULL'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'subcategories': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['core.Subcategory']", 'symmetrical': 'False', 'null': 'True', 'related_name': "'categories'", 'blank': 'True'})
        },
        'core.detail': {
            'Meta': {'object_name': 'Detail'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'facts': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'title_image': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Image']", 'unique': 'True', 'null': 'True', 'blank': 'True', 'on_delete': 'models.SET_NULL'}),
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
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'details': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['core.Detail']", 'symmetrical': 'False', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'materials.material': {
            'Meta': {'object_name': 'Material', '_ormbases': ['core.Category']},
            'category_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Category']", 'unique': 'True', 'primary_key': 'True'})
        },
        'materials.materialdetail': {
            'Meta': {'object_name': 'MaterialDetail', '_ormbases': ['core.Detail']},
            'detail_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Detail']", 'unique': 'True', 'primary_key': 'True'})
        },
        'materials.materialsubcategory': {
            'Meta': {'object_name': 'MaterialSubcategory', '_ormbases': ['core.Subcategory']},
            'subcategory_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Subcategory']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['materials']