# Generated by Django 5.1 on 2024-08-12 18:12

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_rename_user_register_time_enter_person_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="register_time_enter",
            name="description",
            field=ckeditor.fields.RichTextField(
                blank=True, null=True, verbose_name="توضیحات "
            ),
        ),
    ]