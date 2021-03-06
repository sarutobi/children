# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'TimeTable.workshop'
        db.add_column(u'core_timetable', 'workshop',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['core.Workshop']),
                      keep_default=False)

        # Removing M2M table for field sheduled on 'Workshop'
        db.delete_table('core_workshop_sheduled')


    def backwards(self, orm):
        # Deleting field 'TimeTable.workshop'
        db.delete_column(u'core_timetable', 'workshop_id')

        # Adding M2M table for field sheduled on 'Workshop'
        db.create_table(u'core_workshop_sheduled', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('workshop', models.ForeignKey(orm[u'core.workshop'], null=False)),
            ('timetable', models.ForeignKey(orm[u'core.timetable'], null=False))
        ))
        db.create_unique(u'core_workshop_sheduled', ['workshop_id', 'timetable_id'])


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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Organization']"}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['core']