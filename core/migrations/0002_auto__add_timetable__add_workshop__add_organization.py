# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TimeTable'
        db.create_table(u'core_timetable', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('day', self.gf('django.db.models.fields.IntegerField')()),
            ('start_time', self.gf('django.db.models.fields.TimeField')()),
            ('finish_time', self.gf('django.db.models.fields.TimeField')()),
        ))
        db.send_create_signal(u'core', ['TimeTable'])

        # Adding model 'Workshop'
        db.create_table(u'core_workshop', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('organization', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Organization'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'core', ['Workshop'])

        # Adding M2M table for field sheduled on 'Workshop'
        db.create_table(u'core_workshop_sheduled', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('workshop', models.ForeignKey(orm[u'core.workshop'], null=False)),
            ('timetable', models.ForeignKey(orm[u'core.timetable'], null=False))
        ))
        db.create_unique(u'core_workshop_sheduled', ['workshop_id', 'timetable_id'])

        # Adding model 'Organization'
        db.create_table(u'core_organization', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'core', ['Organization'])


    def backwards(self, orm):
        # Deleting model 'TimeTable'
        db.delete_table(u'core_timetable')

        # Deleting model 'Workshop'
        db.delete_table(u'core_workshop')

        # Removing M2M table for field sheduled on 'Workshop'
        db.delete_table('core_workshop_sheduled')

        # Deleting model 'Organization'
        db.delete_table(u'core_organization')


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
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Organization']"}),
            'sheduled': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.TimeTable']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['core']