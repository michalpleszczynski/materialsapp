# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        db.execute("""CREATE MATERIALIZED VIEW unique_detail_words AS SELECT word
        FROM ts_stat('SELECT to_tsvector(''simple'', name) FROM core_detail');""")
        # db.execute("""CREATE MATERIALIZED VIEW unique_subcategory_words AS SELECT word
        # FROM ts_stat('SELECT to_tsvector(''simple'', name) FROM core_subcategory');""")
        # db.execute("""CREATE MATERIALIZED VIEW unique_category_words AS SELECT word
        # FROM ts_stat('SELECT to_tsvector(''simple'', name) FROM core_category');""")

        db.execute("CREATE INDEX detail_words_idx ON unique_detail_words USING gin(word gin_trgm_ops);")
        # db.execute("CREATE INDEX subcategory_words_idx ON unique_subcategory_words USING gin(word gin_trgm_ops);")
        # db.execute("CREATE INDEX category_words_idx ON unique_category_words USING gin(word gin_trgm_ops);")

    def backwards(self, orm):
        db.execute("DROP MATERIALIZED VIEW unique_detail_words;")
        # db.execute("DROP MATERIALIZED VIEW unique_subcategory_words;")
        # db.execute("DROP MATERIALIZED VIEW unique_category_words;")

    models = {
        u'core.category': {
            'Meta': {'object_name': 'Category'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Image']", 'unique': 'True', 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'subcategories': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "u'categories'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['core.Subcategory']"})
        },
        u'core.detail': {
            'Meta': {'object_name': 'Detail'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'facts': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'title_image': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Image']", 'unique': 'True', 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'video_url': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'core.detailsection': {
            'Meta': {'object_name': 'DetailSection'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'detail': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'sections'", 'to': u"orm['core.Detail']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'})
        },
        u'core.detailsectionimage': {
            'Meta': {'object_name': 'DetailSectionImage', '_ormbases': [u'core.Image']},
            u'image_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Image']", 'unique': 'True', 'primary_key': 'True'}),
            'subcategory': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'images'", 'to': u"orm['core.DetailSection']"})
        },
        u'core.image': {
            'Meta': {'object_name': 'Image'},
            'alt_text': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'figcaption': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'core.subcategory': {
            'Meta': {'object_name': 'Subcategory'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'details': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['core.Detail']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        }
    }

    complete_apps = ['core']