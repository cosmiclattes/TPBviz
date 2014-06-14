# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'TPBTopList.attrNoOfComments'
        db.alter_column(u'viz_tpbtoplist', 'attrNoOfComments', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'TPBTopList.attrNoOfComments'
        raise RuntimeError("Cannot reverse this migration. 'TPBTopList.attrNoOfComments' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'TPBTopList.attrNoOfComments'
        db.alter_column(u'viz_tpbtoplist', 'attrNoOfComments', self.gf('django.db.models.fields.PositiveSmallIntegerField')())

    models = {
        u'viz.tpbtoplist': {
            'Meta': {'object_name': 'TPBTopList'},
            'attrCats': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'attrNoOfComments': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'attrTpbStatus': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'hasCover': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'infoHash': ('django.db.models.fields.CharField', [], {'max_length': '40', 'primary_key': 'True'}),
            'leechers': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'seeders': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'size': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'torrentUrl': ('django.db.models.fields.TextField', [], {}),
            'trackerOthers': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'trackerUrl1': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'trackerUrl2': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'trackerUrl3': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'uploadedDate': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'uploadedTime': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'})
        }
    }

    complete_apps = ['viz']