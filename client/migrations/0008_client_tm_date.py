# Generated by Django 4.2.7 on 2023-12-21 04:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("client", "0007_delete_uploadedarchive"),
    ]

    operations = [
        migrations.AddField(
            model_name="client",
            name="tm_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]