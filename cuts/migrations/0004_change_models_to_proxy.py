# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'CutDetail'
        db.delete_table(u'cuts_cutdetail')

        # Deleting model 'CutSubcategory'
        db.delete_table(u'cuts_cutsubcategory')


    def backwards(self, orm):
        # Adding model 'CutDetail'
        db.create_table(u'cuts_cutdetail', (
            (u'detail_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Detail'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'cuts', ['CutDetail'])

        # Adding model 'CutSubcategory'
        db.create_table(u'cuts_cutsubcategory', (
            (u'subcategory_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Subcategory'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'cuts', ['CutSubcategory'])


    models = {
        
    }

    complete_apps = ['cuts']