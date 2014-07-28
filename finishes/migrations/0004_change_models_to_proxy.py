# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'FinishSubcategory'
        db.delete_table(u'finishes_finishsubcategory')

        # Deleting model 'FinishDetail'
        db.delete_table(u'finishes_finishdetail')


    def backwards(self, orm):
        # Adding model 'FinishSubcategory'
        db.create_table(u'finishes_finishsubcategory', (
            (u'subcategory_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Subcategory'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'finishes', ['FinishSubcategory'])

        # Adding model 'FinishDetail'
        db.create_table(u'finishes_finishdetail', (
            (u'detail_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Detail'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'finishes', ['FinishDetail'])


    models = {
        
    }

    complete_apps = ['finishes']