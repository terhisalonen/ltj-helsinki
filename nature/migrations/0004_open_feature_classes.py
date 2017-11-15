# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-15 14:07
from __future__ import unicode_literals

from django.db import migrations

open_feature_classes = [
    'METS',
    'MASA',
    'LSO',
    'BK',
    'EK',
    'GK',
    'KK',
    'LAH',
    'LJH',
    'LJR',
    'LK',
    'LVK',
    'MUU',
    'PM',
    'PPM',
    'PPO',
    'PPV',
    'PPVO',
    'LEPA',
    'KAAP',
    'ROSK',
    'PPUT',
    'LIIT',
    'LITO',
    'LI_P',
    'KUNN',
    'MVER',
    'MYHD',
    'MLAA',
    'VYHT',
    'HULE',
    'LAM',
    'Lmm',
    'Lsa',
    'LslLt',
    'Muu',
    'Natur',
    'Kaava',
    'Lintu',
]


def set_open_feature_classes(apps, schema_editor):
    FeatureClass = apps.get_model('nature', 'FeatureClass')
    FeatureClass.objects.filter(id__in=open_feature_classes).update(open_data=True)


def reset_open_feature_classes(apps, schema_editor):
    FeatureClass = apps.get_model('nature', 'FeatureClass')
    FeatureClass.objects.filter(id__in=open_feature_classes).update(open_data=False)


class Migration(migrations.Migration):
    dependencies = [
        ('nature', '0003_featureclass_open_data'),
    ]

    operations = [
        migrations.RunPython(set_open_feature_classes, reset_open_feature_classes)
    ]
