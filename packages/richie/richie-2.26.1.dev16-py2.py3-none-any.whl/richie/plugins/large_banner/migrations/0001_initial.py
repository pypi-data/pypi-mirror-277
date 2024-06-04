# Generated by Django 2.1.5 on 2019-02-09 08:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import filer.fields.image


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("cms", "0022_auto_20180620_1551"),
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="LargeBanner",
            fields=[
                (
                    "cmsplugin_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        related_name="large_banner_largebanner",
                        serialize=False,
                        to="cms.CMSPlugin",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("logo_alt_text", models.CharField(max_length=255)),
                (
                    "background_image",
                    filer.fields.image.FilerImageField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="background_image",
                        to=settings.FILER_IMAGE_MODEL,
                        verbose_name="background image",
                    ),
                ),
                (
                    "logo",
                    filer.fields.image.FilerImageField(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="logo",
                        to=settings.FILER_IMAGE_MODEL,
                        verbose_name="logo",
                    ),
                ),
            ],
            options={"abstract": False},
            bases=("cms.cmsplugin",),
        )
    ]
