# Generated by Django 4.1.7 on 2023-02-27 19:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="RecordSetting",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "headings",
                    models.CharField(
                        default="personal, work",
                        help_text="Required. Comma separated list of default headings to use.",
                        max_length=300,
                        verbose_name="record headings",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="record_settings",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "record setting",
                "verbose_name_plural": "record settings",
            },
        ),
        migrations.CreateModel(
            name="Record",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                (
                    "title",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="record title"
                    ),
                ),
                (
                    "content",
                    models.TextField(blank=True, verbose_name="record content"),
                ),
                ("date", models.DateField(verbose_name="record date")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="records",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "record",
                "verbose_name_plural": "records",
                "unique_together": {("user", "date")},
            },
        ),
    ]