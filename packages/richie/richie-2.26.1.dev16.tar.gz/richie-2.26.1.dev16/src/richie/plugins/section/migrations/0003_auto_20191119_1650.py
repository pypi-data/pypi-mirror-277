# Generated by Django 2.2.7 on 2019-11-19 15:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("section", "0002_add_template_field"),
    ]

    operations = [
        migrations.AlterField(
            model_name="section",
            name="title",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
