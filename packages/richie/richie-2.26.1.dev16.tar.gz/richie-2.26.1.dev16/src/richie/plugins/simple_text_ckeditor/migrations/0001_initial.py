# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-19 09:28
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [("cms", "0020_old_tree_cleanup")]

    operations = [
        migrations.CreateModel(
            name="SimpleText",
            fields=[
                (
                    "cmsplugin_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        related_name="simple_text_ckeditor_simpletext",
                        serialize=False,
                        to="cms.CMSPlugin",
                    ),
                ),
                ("body", models.TextField(verbose_name="body")),
            ],
            options={"abstract": False},
            bases=("cms.cmsplugin",),
        )
    ]
