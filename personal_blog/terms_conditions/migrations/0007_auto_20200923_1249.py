# Generated by Django 3.0.7 on 2020-09-23 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("terms_conditions", "0006_auto_20200923_1239"),
    ]

    operations = [
        migrations.RenameField(
            model_name="termcondition", old_name="terms", new_name="text",
        ),
    ]
