# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table('core_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('image', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['core.Image'], null=True, blank=True, on_delete=models.SET_NULL)),
        ))
        db.send_create_signal('core', ['Category'])

        # Adding M2M table for field subcategories on 'Category'
        m2m_table_name = db.shorten_name('core_category_subcategories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('category', models.ForeignKey(orm['core.category'], null=False)),
            ('subcategory', models.ForeignKey(orm['core.subcategory'], null=False))
        ))
        db.create_unique(m2m_table_name, ['category_id', 'subcategory_id'])

        # Adding model 'Subcategory'
        db.create_table('core_subcategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
        ))
        db.send_create_signal('core', ['Subcategory'])

        # Adding M2M table for field details on 'Subcategory'
        m2m_table_name = db.shorten_name('core_subcategory_details')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('subcategory', models.ForeignKey(orm['core.subcategory'], null=False)),
            ('detail', models.ForeignKey(orm['core.detail'], null=False))
        ))
        db.create_unique(m2m_table_name, ['subcategory_id', 'detail_id'])

        # Adding model 'Detail'
        db.create_table('core_detail', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('title_image', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['core.Image'], null=True, blank=True, on_delete=models.SET_NULL)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('facts', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('video_url', self.gf('django.db.models.fields.URLField')(max_length=255)),
        ))
        db.send_create_signal('core', ['Detail'])

        # Adding model 'DetailSection'
        db.create_table('core_detailsection', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('detail', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sections', to=orm['core.Detail'])),
        ))
        db.send_create_signal('core', ['DetailSection'])

        # Adding model 'Image'
        db.create_table('core_image', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('alt_text', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('figcaption', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('core', ['Image'])

        # Adding model 'DetailSectionImage'
        db.create_table('core_detailsectionimage', (
            ('image_ptr', self.gf('django.db.models.fields.related.OneToOneField')(primary_key=True, unique=True, to=orm['core.Image'])),
            ('subcategory', self.gf('django.db.models.fields.related.ForeignKey')(related_name='images', to=orm['core.DetailSection'])),
        ))
        db.send_create_signal('core', ['DetailSectionImage'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table('core_category')

        # Removing M2M table for field subcategories on 'Category'
        db.delete_table(db.shorten_name('core_category_subcategories'))

        # Deleting model 'Subcategory'
        db.delete_table('core_subcategory')

        # Removing M2M table for field details on 'Subcategory'
        db.delete_table(db.shorten_name('core_subcategory_details'))

        # Deleting model 'Detail'
        db.delete_table('core_detail')

        # Deleting model 'DetailSection'
        db.delete_table('core_detailsection')

        # Deleting model 'Image'
        db.delete_table('core_image')

        # Deleting model 'DetailSectionImage'
        db.delete_table('core_detailsectionimage')


    models = {
        'core.category': {
            'Meta': {'object_name': 'Category'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['core.Image']", 'null': 'True', 'blank': 'True', 'on_delete': 'models.SET_NULL'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'subcategories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'categories'", 'to': "orm['core.Subcategory']", 'null': 'True', 'blank': 'True'})
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
            'title_image': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['core.Image']", 'null': 'True', 'blank': 'True', 'on_delete': 'models.SET_NULL'}),
            'video_url': ('django.db.models.fields.URLField', [], {'max_length': '255'})
        },
        'core.detailsection': {
            'Meta': {'object_name': 'DetailSection'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'detail': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sections'", 'to': "orm['core.Detail']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'})
        },
        'core.detailsectionimage': {
            'Meta': {'object_name': 'DetailSectionImage', '_ormbases': ['core.Image']},
            'image_ptr': ('django.db.models.fields.related.OneToOneField', [], {'primary_key': 'True', 'unique': 'True', 'to': "orm['core.Image']"}),
            'subcategory': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': "orm['core.DetailSection']"})
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
            'details': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['core.Detail']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        }
    }

    complete_apps = ['core']