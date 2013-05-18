# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'GroupOfInterest'
        db.create_table(u'core_groupofinterest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal(u'core', ['GroupOfInterest'])

        # Adding model 'Interest'
        db.create_table(u'core_interest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('root', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.GroupOfInterest'])),
        ))
        db.send_create_signal(u'core', ['Interest'])


    def backwards(self, orm):
        # Deleting model 'GroupOfInterest'
        db.delete_table(u'core_groupofinterest')

        # Deleting model 'Interest'
        db.delete_table(u'core_interest')


    models = {
        u'core.groupofinterest': {
            'Meta': {'object_name': 'GroupOfInterest'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'core.interest': {
            'Meta': {'object_name': 'Interest'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'root': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.GroupOfInterest']"})
        }
    }

    complete_apps = ['core']