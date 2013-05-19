# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Workshop.min_age'
        db.add_column(u'core_workshop', 'min_age',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Workshop.max_age'
        db.add_column(u'core_workshop', 'max_age',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Workshop.min_age'
        db.delete_column(u'core_workshop', 'min_age')

        # Deleting field 'Workshop.max_age'
        db.delete_column(u'core_workshop', 'max_age')


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
        u'core.interestoskill': {
            'Meta': {'unique_together': "(('skill', 'interest'),)", 'object_name': 'InteresToSkill'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interest': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Interest']"}),
            'ratio': ('django.db.models.fields.FloatField', [], {}),
            'skill': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.Skill']"})
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
            'start_time': ('django.db.models.fields.TimeField', [], {}),
            'workshop': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Workshop']"})
        },
        u'core.workshop': {
            'Meta': {'object_name': 'Workshop'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instructor': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'interests': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Interest']", 'symmetrical': 'False'}),
            'max_age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'min_age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Organization']"}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'users.skill': {
            'Meta': {'object_name': 'Skill'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['core']