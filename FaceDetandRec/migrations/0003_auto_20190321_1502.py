# Generated by Django 2.0.4 on 2019-03-21 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FaceDetandRec', '0002_auto_20190321_1427'),
    ]

    operations = [
        migrations.RenameField(
            model_name='oripic',
            old_name='image',
            new_name='imageOri',
        ),
        migrations.RenameField(
            model_name='tarpic',
            old_name='image',
            new_name='imageTar',
        ),
    ]