# Generated by Django 4.0.4 on 2022-05-05 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user_accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="kanvasuser",
            name="is_admin",
            field=models.BooleanField(default=False),
        ),
    ]