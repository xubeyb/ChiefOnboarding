# Generated by Django 3.2.8 on 2021-11-11 02:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("badges", "0002_badge_polymorphic_ctype"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="badge",
            name="polymorphic_ctype",
        ),
    ]