# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TPBTopList'
        db.create_table(u'viz_tpbtoplist', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('hasCover', self.gf('django.db.models.fields.BooleanField')()),
            ('leechers', self.gf('django.db.models.fields.IntegerField')()),
            ('seeders', self.gf('django.db.models.fields.IntegerField')()),
            ('trackerUrl1', self.gf('django.db.models.fields.TextField')()),
            ('trackerUrl2', self.gf('django.db.models.fields.TextField')()),
            ('trackerUrl3', self.gf('django.db.models.fields.TextField')()),
            ('trackerOthers', self.gf('django.db.models.fields.TextField')()),
            ('uploadedDate', self.gf('django.db.models.fields.DateField')()),
            ('uploadedTime', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('torrentUrl', self.gf('django.db.models.fields.TextField')()),
            ('infoHash', self.gf('django.db.models.fields.CharField')(max_length=40, primary_key=True)),
            ('attrStatus', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('attrNoOfComments', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('attrCats', self.gf('django.db.models.fields.TextField')()),
            ('size', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'viz', ['TPBTopList'])


    def backwards(self, orm):
        # Deleting model 'TPBTopList'
        db.delete_table(u'viz_tpbtoplist')


    models = {
        u'viz.tpbtoplist': {
            'Meta': {'object_name': 'TPBTopList'},
            'attrCats': ('django.db.models.fields.TextField', [], {}),
            'attrNoOfComments': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'attrStatus': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'hasCover': ('django.db.models.fields.BooleanField', [], {}),
            'infoHash': ('django.db.models.fields.CharField', [], {'max_length': '40', 'primary_key': 'True'}),
            'leechers': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'seeders': ('django.db.models.fields.IntegerField', [], {}),
            'size': ('django.db.models.fields.IntegerField', [], {}),
            'torrentUrl': ('django.db.models.fields.TextField', [], {}),
            'trackerOthers': ('django.db.models.fields.TextField', [], {}),
            'trackerUrl1': ('django.db.models.fields.TextField', [], {}),
            'trackerUrl2': ('django.db.models.fields.TextField', [], {}),
            'trackerUrl3': ('django.db.models.fields.TextField', [], {}),
            'uploadedDate': ('django.db.models.fields.DateField', [], {}),
            'uploadedTime': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['viz']