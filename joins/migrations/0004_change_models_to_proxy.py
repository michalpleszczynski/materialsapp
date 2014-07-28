# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'JoinDetail'
        db.delete_table(u'joins_joindetail')

        # Deleting model 'JoinSubcategory'
        db.delete_table(u'joins_joinsubcategory')


    def backwards(self, orm):
        # Adding model 'JoinDetail'
        db.create_table(u'joins_joindetail', (
            (u'detail_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Detail'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'joins', ['JoinDetail'])

        # Adding model 'JoinSubcategory'
        db.create_table(u'joins_joinsubcategory', (
            (u'subcategory_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Subcategory'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'joins', ['JoinSubcategory'])


    models = {
        
    }

    complete_apps = ['joins']