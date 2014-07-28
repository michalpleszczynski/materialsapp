# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'MaterialDetail'
        db.delete_table(u'materials_materialdetail')

        # Deleting model 'Material'
        db.delete_table(u'materials_material')

        # Deleting model 'MaterialSubcategory'
        db.delete_table(u'materials_materialsubcategory')


    def backwards(self, orm):
        # Adding model 'MaterialDetail'
        db.create_table(u'materials_materialdetail', (
            (u'detail_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Detail'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'materials', ['MaterialDetail'])

        # Adding model 'Material'
        db.create_table(u'materials_material', (
            (u'category_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Category'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'materials', ['Material'])

        # Adding model 'MaterialSubcategory'
        db.create_table(u'materials_materialsubcategory', (
            (u'subcategory_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Subcategory'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'materials', ['MaterialSubcategory'])


    models = {
        
    }

    complete_apps = ['materials']