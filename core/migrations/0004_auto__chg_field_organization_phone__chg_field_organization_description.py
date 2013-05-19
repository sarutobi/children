# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Organization.phone'
        db.alter_column(u'core_organization', 'phone', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Organization.description'
        db.alter_column(u'core_organization', 'description', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Workshop.phone'
        db.alter_column(u'core_workshop', 'phone', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Workshop.address'
        db.alter_column(u'core_workshop', 'address', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Organization.phone'
        raise RuntimeError("Cannot reverse this migration. 'Organization.phone' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Organization.description'
        raise RuntimeError("Cannot reverse this migration. 'Organization.description' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Workshop.phone'
        raise RuntimeError("Cannot reverse this migration. 'Workshop.phone' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Workshop.address'
        raise RuntimeError("Cannot reverse this migration. 'Workshop.address' and its values cannot be restored.")

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
        },
        u'core.organization': {
            'Meta': {'object_name': 'Organization'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'core.timetable': {
            'Meta': {'ordering': "('day', 'start_time')", 'object_name': 'TimeTable'},
            'day': ('django.db.models.fields.IntegerField', [], {}),
            'finish_time': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_time': ('django.db.models.fields.TimeField', [], {})
        },
        u'core.workshop': {
            'Meta': {'object_name': 'Workshop'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Organization']"}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'sheduled': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.TimeTable']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['core']