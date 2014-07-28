# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'FormDetail'
        db.delete_table(u'forms_formdetail')

        # Deleting model 'FormSubcategory'
        db.delete_table(u'forms_formsubcategory')


    def backwards(self, orm):
        # Adding model 'FormDetail'
        db.create_table(u'forms_formdetail', (
            (u'detail_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Detail'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'forms', ['FormDetail'])

        # Adding model 'FormSubcategory'
        db.create_table(u'forms_formsubcategory', (
            (u'subcategory_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Subcategory'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'forms', ['FormSubcategory'])


    models = {
        
    }

    complete_apps = ['forms']