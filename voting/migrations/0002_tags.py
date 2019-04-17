# Generated by Django 2.0.4 on 2018-06-13 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_title', models.CharField(max_length=128, unique=True)),
                ('tag_description', models.TextField(null=True)),
                ('tag_sentiment_index', models.FloatField(default=0)),
                ('tag_opposite', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='voting.Tags')),
            ],
        ),
    ]
