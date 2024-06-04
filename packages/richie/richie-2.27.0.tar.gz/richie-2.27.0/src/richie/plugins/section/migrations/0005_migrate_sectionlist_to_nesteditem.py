# Generated by Django 2.2.11 on 2020-03-27 00:28
from django.db import migrations

from ..defaults import SECTION_TEMPLATES


def forwards_func(apps, schema_editor):
    """
    Update every section object which used the deprecated "section_list"
    template to default section template (the first item from choices).
    """
    Section = apps.get_model("section", "Section")

    Section.objects.filter(template="richie/section/section_list.html").update(
        template=SECTION_TEMPLATES[0][0]
    )


class Migration(migrations.Migration):
    dependencies = [
        ("section", "0004_remove_section_cadenced"),
    ]

    operations = [migrations.RunPython(forwards_func, migrations.RunPython.noop)]
