# Generated by Django 2.2.4 on 2019-08-23 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("organizer", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="startup",
            name="logo",
            field=models.FileField(null=True, upload_to=""),
        )
    ]
