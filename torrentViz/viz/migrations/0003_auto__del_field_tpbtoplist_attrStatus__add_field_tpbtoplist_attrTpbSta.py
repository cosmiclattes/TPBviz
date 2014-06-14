# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'TPBTopList.attrStatus'
        db.delete_column(u'viz_tpbtoplist', 'attrStatus')

        # Adding field 'TPBTopList.attrTpbStatus'
        db.add_column(u'viz_tpbtoplist', 'attrTpbStatus',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True),
                      keep_default=False)


        # Changing field 'TPBTopList.trackerOthers'
        db.alter_column(u'viz_tpbtoplist', 'trackerOthers', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'TPBTopList.uploadedDate'
        db.alter_column(u'viz_tpbtoplist', 'uploadedDate', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'TPBTopList.trackerUrl2'
        db.alter_column(u'viz_tpbtoplist', 'trackerUrl2', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'TPBTopList.uploadedTime'
        db.alter_column(u'viz_tpbtoplist', 'uploadedTime', self.gf('django.db.models.fields.CharField')(max_length=20, null=True))

        # Changing field 'TPBTopList.trackerUrl1'
        db.alter_column(u'viz_tpbtoplist', 'trackerUrl1', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'TPBTopList.trackerUrl3'
        db.alter_column(u'viz_tpbtoplist', 'trackerUrl3', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'TPBTopList.attrCats'
        db.alter_column(u'viz_tpbtoplist', 'attrCats', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'TPBTopList.size'
        db.alter_column(u'viz_tpbtoplist', 'size', self.gf('django.db.models.fields.IntegerField')(null=True))

    def backwards(self, orm):
        # Adding field 'TPBTopList.attrStatus'
        db.add_column(u'viz_tpbtoplist', 'attrStatus',
                      self.gf('django.db.models.fields.CharField')(default='VIP', max_length=20),
                      keep_default=False)

        # Deleting field 'TPBTopList.attrTpbStatus'
        db.delete_column(u'viz_tpbtoplist', 'attrTpbStatus')


        # User chose to not deal with backwards NULL issues for 'TPBTopList.trackerOthers'
        raise RuntimeError("Cannot reverse this migration. 'TPBTopList.trackerOthers' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'TPBTopList.trackerOthers'
        db.alter_column(u'viz_tpbtoplist', 'trackerOthers', self.gf('django.db.models.fields.TextField')())

        # User chose to not deal with backwards NULL issues for 'TPBTopList.uploadedDate'
        raise RuntimeError("Cannot reverse this migration. 'TPBTopList.uploadedDate' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'TPBTopList.uploadedDate'
        db.alter_column(u'viz_tpbtoplist', 'uploadedDate', self.gf('django.db.models.fields.DateField')())

        # User chose to not deal with backwards NULL issues for 'TPBTopList.trackerUrl2'
        raise RuntimeError("Cannot reverse this migration. 'TPBTopList.trackerUrl2' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'TPBTopList.trackerUrl2'
        db.alter_column(u'viz_tpbtoplist', 'trackerUrl2', self.gf('django.db.models.fields.TextField')())

        # User chose to not deal with backwards NULL issues for 'TPBTopList.uploadedTime'
        raise RuntimeError("Cannot reverse this migration. 'TPBTopList.uploadedTime' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'TPBTopList.uploadedTime'
        db.alter_column(u'viz_tpbtoplist', 'uploadedTime', self.gf('django.db.models.fields.CharField')(max_length=20))

        # User chose to not deal with backwards NULL issues for 'TPBTopList.trackerUrl1'
        raise RuntimeError("Cannot reverse this migration. 'TPBTopList.trackerUrl1' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'TPBTopList.trackerUrl1'
        db.alter_column(u'viz_tpbtoplist', 'trackerUrl1', self.gf('django.db.models.fields.TextField')())

        # User chose to not deal with backwards NULL issues for 'TPBTopList.trackerUrl3'
        raise RuntimeError("Cannot reverse this migration. 'TPBTopList.trackerUrl3' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'TPBTopList.trackerUrl3'
        db.alter_column(u'viz_tpbtoplist', 'trackerUrl3', self.gf('django.db.models.fields.TextField')())

        # User chose to not deal with backwards NULL issues for 'TPBTopList.attrCats'
        raise RuntimeError("Cannot reverse this migration. 'TPBTopList.attrCats' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'TPBTopList.attrCats'
        db.alter_column(u'viz_tpbtoplist', 'attrCats', self.gf('django.db.models.fields.TextField')())

        # User chose to not deal with backwards NULL issues for 'TPBTopList.size'
        raise RuntimeError("Cannot reverse this migration. 'TPBTopList.size' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'TPBTopList.size'
        db.alter_column(u'viz_tpbtoplist', 'size', self.gf('django.db.models.fields.IntegerField')())

    models = {
        u'viz.tpbtoplist': {
            'Meta': {'object_name': 'TPBTopList'},
            'attrCats': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'attrNoOfComments': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'attrTpbStatus': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'hasCover': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'infoHash': ('django.db.models.fields.CharField', [], {'max_length': '40', 'primary_key': 'True'}),
            'leechers': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'seeders': ('django.db.models.fields.IntegerField', [], {}),
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