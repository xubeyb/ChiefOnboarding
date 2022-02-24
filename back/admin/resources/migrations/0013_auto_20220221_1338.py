# Generated by Django 3.2.12 on 2022-02-21 13:38

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0012_auto_20220215_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='resources.category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='course',
            field=models.BooleanField(default=False, verbose_name='Is a course item'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='name',
            field=models.CharField(max_length=240, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='on_day',
            field=models.IntegerField(default=0, verbose_name='Workday that this item is due'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='remove_on_complete',
            field=models.BooleanField(default=False, verbose_name='Remove item when new hire walked through'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='tags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10200), blank=True, size=None, verbose_name='Tags'),
        ),
    ]