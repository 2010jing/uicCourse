# Generated by Django 2.0.4 on 2018-06-08 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_coursetype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(default='NULL0000', max_length=32)),
                ('course_name_en', models.CharField(max_length=128, null=True)),
                ('course_name_cn', models.CharField(max_length=128, null=True)),
                ('course_units', models.IntegerField(default=3)),
                ('course_description', models.TextField(null=True)),
                ('is_visible', models.BooleanField(default=True)),
                ('is_rateable', models.BooleanField(default=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('course_major_take', models.ManyToManyField(to='course.ValidDivisionMajorPair')),
                ('course_pre_request', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='course.Course')),
                ('course_type', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='course.CourseType')),
            ],
        ),
    ]