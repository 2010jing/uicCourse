# Generated by Django 2.0.6 on 2018-06-16 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_auto_20180614_2200'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['course_name_en', 'course_id']},
        ),
    ]